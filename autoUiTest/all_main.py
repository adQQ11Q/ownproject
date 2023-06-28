import pytest,os



if __name__ == '__main__':
    pytest.main(["--alluredir","../test_report/result"])
    os.system("allure generate ../test_report/result/ -o ../test_report/report_allure/ --clean")