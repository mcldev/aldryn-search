from packaging.version import Version

import cms


GTE_CMS_35 = Version(cms.__version__) >= Version('3.5')


def is_authenticated(user):
    return user.is_authenticated
