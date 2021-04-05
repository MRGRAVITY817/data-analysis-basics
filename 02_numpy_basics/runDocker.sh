#!/bin/bash
docker run -it \
           --name harry-potter \
           --rm \
           -v $(pwd)/test:/app \
           numpy_basic:1.0

