#init is used for modules (one file with stuff you use) when put all in one directory to turn them into a package
#ps anything in here is automatically run ONCE when you import the package name
from .Chrono import Chrono
from .Sky import Sky
from .Inspire import Inspire
from .Stats import Stats
from .Notify import Notify


# import won't work if run from here but when run from other files it works fine