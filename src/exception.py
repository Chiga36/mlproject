import sys
# import logging
from src.logger import logging
# this is used when we need to log our exception handling 

def error_mssg_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    ## On which file the exception occurred
    ## On which line the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    # this is all custom error handling
    error_mssg=f"Error occured in python script anme [{file_name}] line number [{exc_tb.tb_lineno}] error mssg [{str(error)}]"
    return error_mssg # ****

class CustomException(Exception):
    def __init__(self, error_mssg,error_detail:sys):
        # we are inheriting init func
        super().__init__(error_mssg)
        self.error_mssg = error_mssg_details(error_mssg,error_detail=error_detail)
        # error detail is tracked by sys

    def __str__(self):
        return self.error_mssg


# eg:                                                
# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divided by 0")
#         raise CustomException(e,sys)