from os import path
import src.unchanging_constants as uc
from datetime import datetime
from matplotlib.font_manager import FontProperties
from pandas.api.types import CategoricalDtype

"""Settings for the whole project"""


# USER INPUT SETTINGS
QUIT = 'Q'

WELCOME_MESSAGE = """Welcome to Alex Waygood's interactive data viewer for weekly excess deaths!
This script uses the FT's data. However, the script itself was written by Alex Waygood, and is in no way affiliated with the FT.
"""

LIST_OF_COUNTRIES_QUESTION = "Would you like to see a list of available countries in the FT's dataset? "
ANNOUNCE_LIST_OF_COUNTRIES = "The following countries are available in the FT's dataset: "
COUNTRY_NOT_FOUND_MESSAGE = 'Country not in FT dataset; please try again.'
HOW_MANY_COUNTRIES_MESSAGE = 'Please enter how many countries you want to compare: '
HOW_MANY_COUNTRIES_BUTTON_LABEL = 'Submit'
INVALID_RESPONSE = 'Not a valid response, please try again.'

UNEXPECTED_ERROR_MESSAGE = 'Looks like there was an error here! ' \
                           'Check the log file for more info. Maybe try with different countries?'

METHODOLOGY_MESSAGE = 'For the full details on how these graphs are made,' \
                   'http://covid-excess-deaths.ew.r.appspot.com/about/'


MIN_COUNTRIES = 1
MAX_COUNTRIES = 5
ORDINALS = ('first', 'second', 'third', 'fourth', 'fifth')


def Select_Country_Message(
        i: int,
        CountryNumber: int,
        DesktopUsage: bool
) -> str:

    VERB = 'enter the name of' if DesktopUsage else 'select'

    if CountryNumber == 1:
        return f'Please {VERB} the country you would like to graph'
    return f'Please {VERB} the {ORDINALS[i]} country you would like to compare'


def Desktop_Error_Message(Traceback: str) -> str:
    return f"Exception!\n\n{Traceback}\n\n"


# LOGGING SETTINGS
LOGGING_CONFIG = '%(asctime)-15s %(name)s %(levelname)s %(message)s'


def LogFileName() -> str:
    return path.join('error_logs', f"Covid graph error log - {datetime.now().strftime('%Y-%m-%d')}.txt")


# GENERAL GRAPH SETTINGS
FAVICON_FILE_PATH = path.join('static', 'images', 'coronavirus.ico')
WINDOW_CAPTION = "Alex Waygood's interactive data viewer for excess deaths"
BACKGROUND_COLOUR = '#fdffd4'
STANDARD_TEXT_COLOUR = '#747564'
PATH_TO_STANDARD_FONT = path.join('static', 'PlayfairDisplay-VariableFont_wght.ttf')
STANDARD_FONT = FontProperties(fname=PATH_TO_STANDARD_FONT)

# GRAPH EXPORT SETTINGS
EXPORT_FILE_PATH = path.join('graph_images')
EXPORT_FILE_TYPE = 'png'
WEB_DISPLAY_FILE_TYPE = 'png'


def PNGFilePath() -> str:
    return path.join(
        EXPORT_FILE_PATH,
        f'Covid graph {str(datetime.now()).replace(":", ".")}.{EXPORT_FILE_TYPE}'
    )


# AXES SETTINGS
AXIS_TICK_COLOUR = STANDARD_TEXT_COLOUR
AXIS_FONT = 'serif'
AXIS_TEXT_COLOUR = STANDARD_TEXT_COLOUR

# GRAPH DIMENSIONS SETTINGS
FIGURE_WIDTH = 12
FIGURE_HEIGHT = 6
GRAPH_TOP = 0.8
GRAPH_BOTTOM = 0.25

# TITLE SETTINGS

COUNTRIES_WHICH_NEED_ARTICLE = ('US', 'UK', 'Netherlands', 'Czech Republic', 'Philippines')


def AddArticle(country: str) -> str:
    return f'the {country}' if country in COUNTRIES_WHICH_NEED_ARTICLE else country


def GraphTitle(Countries: uc.STRING_LIST) -> str:
    Countries = list(map(AddArticle, Countries))
    Countries = Countries[0] if len(Countries) == 1 else f'{", ".join(Countries[:-1])} and {Countries[-1]}'
    return f'Pandemic excess deaths in {Countries}'


GRAPH_TITLE_POSITION = 0.93
TITLE_SIZE = 'xx-large'
TITLE_FONT = STANDARD_FONT
TITLE_COLOUR = STANDARD_TEXT_COLOUR

# SUBTITLE SETTINGS
SUB_TITLE = 'Relative to historical average for same dates, %'
SUB_TITLE_PADDING_FROM_GRAPH = 18
SUB_TITLE_COLOUR = STANDARD_TEXT_COLOUR
SUB_TITLE_FONT = STANDARD_FONT

# LEGEND SETTINGS
LEGEND_OPACITY = 1
LEGEND_FONT = STANDARD_FONT
LEGEND_TEXT_COLOUR = STANDARD_TEXT_COLOUR

# DATA SELECTION SETTINGS
FT_DATA_URL = 'https://raw.githubusercontent.com/Financial-Times/coronavirus-excess-mortality-data/master/data/ft_excess_deaths.csv'

FT_DATA_TYPES = {
    uc.EXPECTED_DEATHS: 'float64',
    uc.EXCESS_DEATHS: 'float64',
    uc.TOTAL_EXCESS_DEATHS_PCT: 'float64',
    uc.DATE: object,
    uc.COUNTRY: 'category',
    uc.REGION: object,
    uc.DEATHS: 'float64'
}

# HORIZONTAL LINE SETTINGS
HORIZONTAL_LINE_COLOUR = 'silver'
HORIZONTAL_LINE_WIDTH = 1
HORIZONTAL_LINE_STYLE = 'dashed'
HORIZONTAL_LINE_INCREMENT = 50

X_AXIS_LINE_SYTLE = HORIZONTAL_LINE_STYLE
X_AXIS_COLOUR = 'grey'
X_AXIS_WIDTH = 1.3

# COPYRIGHT LABEL SETTINGS

COPYRIGHT_LABEL = 'Data from the Financial Times | Graph © Alex Waygood\n\n' \
                  'Recent data on excess deaths is likely to be revised upwards in the coming weeks and months.\n'

COPYRIGHT_LABEL_FONT = STANDARD_FONT
COPYRIGHT_LABEL_COLOUR = STANDARD_TEXT_COLOUR
COPYRIGHT_LABEL_PADDING_FROM_X_AXIS = 26

# GRAPH SMOOTHING SETTINGS
# See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate...
# ...For the full range of interpolation methods that can be supplied

# Should be CUBIC or LINEAR
INTERPOLATE_METHODS = (uc.CUBIC, uc.QUADRATIC, uc.SLINEAR)
