# -*- coding: utf-8 -*


class BaseAssert(object):

    assertion_errors = []

    def soft_assert_equals(self, current, expected, msg=None):
        if not current == expected:
            error = (
                u"{msg}\n"
                u"Current - {current}\n"
                u"Expected - {expected}\n".format(
                    msg=msg,
                    current=current,
                    expected=expected
                    )
            )
            if type(current) != type(expected):
                error += (
                    u"Current and expected has different data types: "
                    u"current is %s, expected is %s" % (
                        type(current), type(expected)
                    )
                )
            self.assertion_errors.append(error)
            return error
        return None
