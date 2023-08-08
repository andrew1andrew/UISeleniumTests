FROM python
WORKDIR /container_tests/
COPY . .
RUN pip install -r requirements.txt
CMD python -m pytest -s --alluredir=allure_results/ Tests/Positive_cases/*