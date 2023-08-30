FROM python:3.10-alpine
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories \
    && apk update \
    && apk add chromium chromium-chromedriver
WORKDIR /container_tests/
COPY . .
RUN pip install -r requirements.txt
CMD python -m pytest -s --alluredir=allure_results/ /container_tests/Tests/Positive_cases/Test*
CMD python -m pytest -s --alluredir=allure_results/ /container_tests/Tests/Negative_cases/Test*
