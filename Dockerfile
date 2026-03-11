FROM ubuntu:latest
LABEL authors="p4elk"

ENTRYPOINT ["top", "-b"]