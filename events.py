class EventHook(object):
    def __init__(self):
        self._handlers = []

    def __iadd__(self, handler):
        self._handlers.append(handler)
        return self

    def __isub__(self, handler):
        self._handlers.remove(handler)
        return self

    def fire(self, reverse=False, **kwargs):
        if reverse:
            self._handlers.reverse()
        for handler in self._handlers:
            handler(**kwargs)


request_success = EventHook()
"""
*request_success* is fired when a request is completed successfully.

Listeners should take the following arguments:

* *request_type*: Request type method used
* *name*: Path to the URL that was called (or override name if it was used in the call to the client)
* *response_time*: Response time in milliseconds
* *response_length*: Content-length of the response
"""

request_failure = EventHook()
"""
*request_failure* is fired when a request fails

Event is fired with the following arguments:

* *request_type*: Request type method used
* *name*: Path to the URL that was called (or override name if it was used in the call to the client)
* *response_time*: Time in milliseconds until exception was thrown
* *response_length*: Content-length of the response
* *exception*: Exception instance that was thrown
"""

