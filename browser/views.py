import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import EntityType, Entity, DataFile


def check_accepts_html(request):
    if not "Accept" in request.headers:
        return {}
    
    accept_str = request.headers["Accept"]
    
    # "accept_str" can be something like
    # "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8".
    # We need to split on ";", then on ","

    subitems = []
    for longchunk in accept_str.split(";"):
        for shortchunk in longchunk.split(","):
            subitems.append(shortchunk.lower())

    return "text/html" in subitems

def parse_metadata(metadata_str):
    if metadata_str.strip() != "":
        return json.loads(metadata_str)
    else:
        return {}
    


class EntityTypeListView(ListView):
    model = EntityType
    template_name = "browser/index.html"
    context_object_name = "list_of_types"

class EntityTypeView(DetailView):
    model = EntityType
    template_name = "browser/entity_type_detail.html"

    def get(self, request, pk):
        cur_entity_type = get_object_or_404(EntityType, pk=pk)
        return render(request, self.template_name, {
            "entity_type": cur_entity_type,
            "entities": Entity.objects.filter(kind=cur_entity_type),
        })

class EntityView(DetailView):
    model = Entity
    template_name = "browser/entity_detail.html"
    context_object_name = "entity"

    def get(self, request, pk):
        cur_entity = get_object_or_404(Entity, pk=pk)
        if check_accepts_html(request):
            # HTML page, shown by web browsers
            result = {
                "entity": cur_entity,
                "data_files": DataFile.objects.filter(entity=cur_entity).order_by("-upload_date"),
            }
            return render(request, self.template_name, result)
        else:
             # JSON record, returned by "curl"
            result = {
                "type": "entity",
                "entity": reverse("entity_detail", args=[cur_entity.uuid]),
                "name": cur_entity.name,
                "kind": reverse("entity_type_detail", args=[cur_entity.kind.id]),
                "metadata": parse_metadata(cur_entity.metadata),
            }
            return JsonResponse(result)


class DataFileView(DetailView):
    model = DataFile
    template_name = "browser/data_file_detail.html"
    context_object_name = "data_file"

    def get(self, request, pk):
        cur_data_file = get_object_or_404(DataFile, pk=pk)

        siblings = DataFile.objects.filter(entity=cur_data_file.entity).order_by("-upload_date")
        if siblings and siblings[0] != cur_data_file:
            most_recent_sibling = siblings[0]
        else:
            most_recent_sibling = None

        if check_accepts_html(request):
            # HTML page, shown by web browsers
            result = {
                "data_file": cur_data_file,
                "entity": cur_data_file.entity,
                "entity_type": cur_data_file.entity.kind,
                "dependencies": cur_data_file.dependencies.all(),
                "most_recent_sibling": most_recent_sibling,
            }
            return render(request, self.template_name, result)
        else:
             # JSON record, returned by "curl"
            result = {
                "type": "data_file",
                "uri": reverse("data_file_detail", args=[cur_data_file.uuid]),
                "name": cur_data_file.name,
                "upload_date": cur_data_file.upload_date,
                "metadata": parse_metadata(cur_data_file.metadata),
                "spec_version": cur_data_file.spec_version,
                "entity": reverse("entity_detail", args=[cur_data_file.entity.uuid]),
                "entity_type": cur_data_file.entity.kind.name,
                "notes": cur_data_file.notes,
                "dependencies": [reverse("data_file_detail", args=[x.uuid])
                                 for x in cur_data_file.dependencies.all()],
            }
            return JsonResponse(result)
            
