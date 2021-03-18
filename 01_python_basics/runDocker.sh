#!/bin/bash
docker run -it \
           --name harry-potter \
           --rm \
           -v $(pwd)/test:/app \
           data_analysis:2.0

