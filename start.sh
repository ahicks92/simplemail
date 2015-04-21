#!/bin/bash

NAME="simplemail"                                  # Name of the application
DJANGODIR=/home/camlorn/simplemail/cen4010  #Django project directory
SOCKFILE=/home/camlorn/simplemail/running.sock # we will communicate using this unix socket
USER=camlorn                                        # the user to run as
GROUP=camlorn                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=cen4010.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=cen4010.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR


source $DJANGODIR/../authenticate.sh #set up mailgun key

echo Mailgun key is $mailgun_key

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-file=-
