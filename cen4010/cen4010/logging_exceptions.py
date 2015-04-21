import logging
import traceback

class ExceptionLoggingMiddleware(object):

    def process_exception(self, request, exception):
        logging.debug('Exception handling request for ' + request.path)
        logging.debug(traceback.print_exc(exception))
