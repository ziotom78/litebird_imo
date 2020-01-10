# Mock up for a LiteBIRD Instrument Model (ImO)

This repository contains a proof-of-concept for an Instrument Model to
be used in the [LiteBIRD Mission](http://litebird.jp/eng/). It was
first shown during the Sep 2019 LiteBIRD European Meeting in Santander
(Spain).

It is a Python 3 program written using Django.

## Installation

The project use [poetry](https://python-poetry.org/) to manage all its
dependencies. Once you have installed Poetry, run the following
command to create a dedicated virtual environment and install all the
dependencies:

    cd litebird_imo
    poetry install
    
Then run the server:

    poetry run python3 manage.py makemigrations
    poetry run python3 manage.py migrate
    poetry run python3 manage.py createsuperuser
    poetry run python3 manage.py runserver
    
Start the server by opening the admin webpage:
http://127.0.0.1:8000/admin
    
Then enter as the superuser, then populate the database according to
the following order:

1. Create a few «Entity types» (e.g., `full_beam`,
   `scanning_strategy`, `bandpass`)
2. Create a few «Entities» (e.g., a few bandpasses)
3. Add «data files» to each entity; multiple data files referring to
   the same entity are considered consecutive upgrades.
   
Once you have populated the database, visit the following URL:
http://127.0.0.1:8000/browse and start navigating.

## License

This program is released under the BSD license.

Copyright 2019 Maurizio Tomasi

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
