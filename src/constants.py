PROB_PER_OVER_RANGE = {
	"83-85": 0.20,
	"86-88": 0.35,
	"88-89": 0.35,
	"90-99": 0.10
}

NUMBER_OF_PLAYERS = 4

NUMBER_OF_RES = 7

FORMATIONS = {
        "3-4-3 LOSANGO": ["GOL", "ZAG", "ZAG", "ZAG", "VOL", "MD", "ME", "MEI", "PD", "PE", "ATA"],
        "3-4-3 EM LINHA": ["GOL", "ZAG", "ZAG", "ZAG", "MC", "MC", "MD", "ME", "PD", "PE", "ATA"],
        "3-4-2-1": ["GOL", "ZAG", "ZAG", "ZAG", "MC", "MC", "MD", "ME", "SA", "SA", "ATA"],
        "3-5-1-1": ["GOL", "ZAG", "ZAG", "ZAG", "VOL", "VOL",  "MC", "MD", "ME", "SA", "ATA"],
        "3-5-2": ["GOL", "ZAG", "ZAG", "ZAG", "VOL", "VOL", "MD", "ME", "MEI", "ATA", "ATA"],
        "3-4-1-2": ["GOL", "ZAG", "ZAG", "ZAG", "MC", "MC", "MD", "ME", "MEI", "ATA", "ATA"],
        "3-1-4-2": ["GOL", "ZAG", "ZAG", "ZAG", "VOL", "MC", "MC", "MD", "ME", "ATA", "ATA"],
        "5-2-3": ["GOL", "ZAG", "ZAG", "ZAG", "ADD", "ADE", "MC", "MC", "PD", "PE", "ATA"],
        "5-3-2 CONSERVADOR": ["GOL", "ZAG", "ZAG", "ZAG", "ADD", "ADE", "VOL", "MC", "MC", "ATA", "ATA"],
        "5-2-1-2": ["GOL", "ZAG", "ZAG", "ZAG", "ADD", "ADE", "MC", "MC", "MEI", "ATA", "ATA"],
        "5-1-2-1-1": ["GOL", "ZAG", "ZAG", "ZAG", "ADD", "ADE", "VOL", "MC", "MC", "MEI", "ATA"],
        "5-2-2-1": ["GOL", "ZAG", "ZAG", "ZAG", "ADD", "ADE", "VOL", "VOL", "MEI", "MEI", "ATA"],
        "5-4-1 EM LINHA": ["GOL", "ZAG", "ZAG", "ZAG", "ADD", "ADE", "MC", "MC", "MD", "ME", "ATA"],
        "5-4-1 LOSANGO": ["GOL", "ZAG", "ZAG", "ZAG", "ADD", "ADE", "VOL", "MD", "ME", "MEI", "ATA"],
        "4-2-4": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "PD", "PE", "ATA", "ATA"],
        "4-2-1-3": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "VOL", "MEI" "PD", "PE", "ATA"],
        "4-3-2-1": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MC", "SA", "SA", "ATA"],
        "4-3-3 EM LINHA": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MC", "PD", "PE", "ATA"],
        "4-3-3 CONSERVADOR": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "MC", "MC", "PD", "PE", "ATA"],
        "4-3-3 DEFENSIVO": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "VOL", "MC", "PD", "PE", "ATA"],
        "4-3-3 OFENSIVO": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MEI", "PD", "PE", "ATA"],
        "4-3-3 FALSO 9": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "MC", "MC", "PD", "PE", "SA"],
        "4-1-3-2": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "MC", "MD", "ME", "ATA", "ATA"],
        "4-3-1-2": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MC", "MEI", "ATA", "ATA"],
        "4-2-2-2": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "VOL", "MEI", "MEI", "ATA", "ATA"],
        "4-1-2-1-2 ABERTO": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "MD", "ME", "MEI", "ATA", "ATA"],
        "4-1-2-1-2 FECHADO": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "MC", "MC", "MEI", "ATA", "ATA"],
        "4-4-2 EM LINHA": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MD", "ME", "ATA", "ATA"],
        "4-4-2 CONSERVADOR": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "VOL", "MD", "ME", "ATA", "ATA"],
        "4-4-1-1 OFENSIVO": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MD", "ME", "SA", "ATA"],
        "4-4-1-1 MEIO-CAMPO": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MD", "ME", "MEI", "ATA"],
        "4-5-1 EM LINHA": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MC", "MC", "MD", "ME", "ATA"],
        "4-5-1 OFENSIVO": ["GOL", "ZAG", "ZAG", "LD", "LE", "MC", "MD", "ME", "MEI", "MEI", "ATA"],
        "4-2-3-1 ABERTO": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "VOL", "MD", "ME", "MEI", "ATA"],
        "4-2-3-1 ABERTO": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "VOL", "MEI", "MEI", "MEI", "ATA"],
        "4-1-4-1": ["GOL", "ZAG", "ZAG", "LD", "LE", "VOL", "MC", "MC", "MD", "ME", "ATA"]
    }

POSITIONS_MAP = {
        "GK":  "GOL",
        "CB":  "ZAG",
        "RB":  "LD",
        "LB":  "LE",
        "RWB": "ADD",
        "LWB": "ADE",
        "CDM": "VOL",
        "CM":  "MC",
        "RM":  "MD",
        "LM":  "ME",
        "CAM": "MEI",
        "RAM": "MAD",
        "LAM": "MAE",
        "RW": "PD",
        "LW": "PE",
        "CF":  "SA",
        "ST":  "ATA"
}

COLLDOWN_TIME = 15*60  # Segundos

PLAYERS = {
    "Felipe",
    "Tharik"
}

APP_INFO = {
    "name": "FIFA Drafter",
    "favicon": "⚽️"
}