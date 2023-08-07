FROM python
WORKDIR /container_tests/
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD python -m pytest -s --alluredir=allure_results/ /container_tests/Tests/Positive_cases