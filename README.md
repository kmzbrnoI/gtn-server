# gtn-server

## Run

    # Linux
    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirements.txt

    # Windows
    py -3 -m venv venv
    venv\Scripts\activate
    pip3 install -r requirements.txt

    python gtn-server


## Local checks

    ./pep8-diff.sh show
    pylint gtn-server
