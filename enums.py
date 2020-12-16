from enum import Enum, auto


class Height(Enum):
    CLOSE = auto()
    NEAR_CLOSE = auto()
    CLOSE_MID = auto()
    MID = auto()
    OPEN_MID = auto()
    NEAR_OPEN = auto()
    OPEN = auto()


class Backness(Enum):
    FRONT = auto()
    CENTRAL = auto()
    BACK = auto()


class Phonation(Enum):
    MODAL = auto()
    BREATHY_VOICE = auto()
    CREAKY_VOICE = auto()

    
class Place(Enum):
    BILABIAL = auto()
    LABIODENTAL = auto()
    LINGUO_LABIAL = auto()
    DENTAL = auto()
    ALVEOLAR = auto()
    POSTALVEOLAR = auto()
    ALVEOLO_PALATAL = auto()
    HISSING_HUSHING = auto()
    RETROFLEX = auto()
    PALATAL = auto()
    VELAR = auto()
    UVULAR = auto()
    PHARYNGEAL = auto()
    EPIGLOTTAL = auto()
    GLOTTAL = auto()


class Manner(Enum):
    PLOSIVE = auto()
    FRICATIVE = auto()
    AFFRICATE = auto()
    APPROXIMANT = auto()
    TAP = auto()
    TRILL = auto()


class Voice(Enum):
    VOICELESS = auto()
    VOICED = auto()
    DEVOICED = auto()


class Length(Enum):
    SHORTENED = auto()
    SHORT = auto()
    HALF_LONG = auto()
    LONG = auto()
    OVERLONG = auto()


class AdditionalArticulation(Enum):
    PRE_ASPIRATED = auto()
    PRE_GLOTTALISED = auto()
    PRE_NASALISED = auto()
    PRE_LABIALISED = auto()
    PHARYNGEALISED = auto()
    NASALISED = auto()
    RAISED = auto()
    LOWERED = auto()
    ADVANCED = auto()
    RETRACTED = auto()
    BREATHY_VOICED = auto()
    VOICELESS = auto()
    CREAKY_VOICED = auto()
    INGRESSIVE = auto()
    RHOTACISED = auto()
    FAUCALISED = auto()
    CENTRALISED = auto()
    ATR = auto()
    RTR = auto()
    LESS_ROUNDED = auto()
    MORE_ROUNDED = auto()
    NON_SYLLABIC = auto()
    MID_CENTRALISED = auto()
    ASPIRATED = auto()
    PALATALISED = auto()
    LABIALISED = auto()
    EJECTIVE = auto()
    GLOTTALISED = auto()
    VELARISED = auto()
    LATERAL_RELEASED = auto()
    UNRELEASED = auto()
    SYLLABIC = auto()
    APICAL = auto()
    LAMINAL = auto()
    WEAKLY_ARTICULATED = auto()
    LABIO_PALATALISED = auto()
    NASAL_RELEASED = auto()
    AFFRICATED = auto()
    EPILARYNGEAL_SOURCE = auto()
    FRICTIONALISED = auto()
    TENUIS = auto()
