docker build --tag python-django . \
&& docker run --publish 7000:7000 python-django