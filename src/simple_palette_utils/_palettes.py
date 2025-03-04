from typing import List, Tuple, Dict, Union
from PIL import ImageColor

# https://en.wikipedia.org/wiki/X11_color_names
X11_COLORS = [
    "#F0F8FF",
    "#FAEBD7",
    "#00FFFF",
    "#7FFFD4",
    "#F0FFFF",
    "#F5F5DC",
    "#FFE4C4",
    "#000000",
    "#FFEBCD",
    "#0000FF",
    "#8A2BE2",
    "#A52A2A",
    "#DEB887",
    "#5F9EA0",
    "#7FFF00",
    "#D2691E",
    "#FF7F50",
    "#6495ED",
    "#FFF8DC",
    "#DC143C",
    "#00FFFF",
    "#00008B",
    "#008B8B",
    "#B8860B",
    "#A9A9A9",
    "#006400",
    "#BDB76B",
    "#8B008B",
    "#556B2F",
    "#FF8C00",
    "#9932CC",
    "#8B0000",
    "#E9967A",
    "#8FBC8F",
    "#483D8B",
    "#2F4F4F",
    "#00CED1",
    "#9400D3",
    "#FF1493",
    "#00BFFF",
    "#696969",
    "#1E90FF",
    "#B22222",
    "#FFFAF0",
    "#228B22",
    "#FF00FF",
    "#DCDCDC",
    "#F8F8FF",
    "#FFD700",
    "#DAA520",
    "#BEBEBE",
    "#808080",
    "#00FF00",
    "#008000",
    "#ADFF2F",
    "#F0FFF0",
    "#FF69B4",
    "#CD5C5C",
    "#4B0082",
    "#FFFFF0",
    "#F0E68C",
    "#E6E6FA",
    "#FFF0F5",
    "#7CFC00",
    "#FFFACD",
    "#ADD8E6",
    "#F08080",
    "#E0FFFF",
    "#FAFAD2",
    "#D3D3D3",
    "#90EE90",
    "#FFB6C1",
    "#FFA07A",
    "#20B2AA",
    "#87CEFA",
    "#778899",
    "#B0C4DE",
    "#FFFFE0",
    "#00FF00",
    "#32CD32",
    "#FAF0E6",
    "#FF00FF",
    "#B03060",
    "#800000",
    "#66CDAA",
    "#0000CD",
    "#BA55D3",
    "#9370DB",
    "#3CB371",
    "#7B68EE",
    "#00FA9A",
    "#48D1CC",
    "#C71585",
    "#191970",
    "#F5FFFA",
    "#FFE4E1",
    "#FFE4B5",
    "#FFDEAD",
    "#000080",
    "#FDF5E6",
    "#808000",
    "#6B8E23",
    "#FFA500",
    "#FF4500",
    "#DA70D6",
    "#EEE8AA",
    "#98FB98",
    "#AFEEEE",
    "#DB7093",
    "#FFEFD5",
    "#FFDAB9",
    "#CD853F",
    "#FFC0CB",
    "#DDA0DD",
    "#B0E0E6",
    "#A020F0",
    "#800080",
    "#663399",
    "#FF0000",
    "#BC8F8F",
    "#4169E1",
    "#8B4513",
    "#FA8072",
    "#F4A460",
    "#2E8B57",
    "#FFF5EE",
    "#A0522D",
    "#C0C0C0",
    "#87CEEB",
    "#6A5ACD",
    "#708090",
    "#FFFAFA",
    "#00FF7F",
    "#4682B4",
    "#D2B48C",
    "#008080",
    "#D8BFD8",
    "#FF6347",
    "#40E0D0",
    "#EE82EE",
    "#F5DEB3",
    "#FFFFFF",
    "#F5F5F5",
    "#FFFF00",
    "#9ACD32",
]

LIGHT_COLORS = [
    "#F0F8FF",
    "#F0FFFF",
    "#F5F5DC",
    "#FFE4C4",
    "#FFEBCD",
    "#FFF8DC",
    "#FFFAF0",
    "#F8F8FF",
    "#F0FFF0",
    "#FFFFF0",
    "#FFF0F5",
    "#E0FFFF",
    "#FFFFE0",
    "#FAF0E6",
    "#F5FFFA",
    "#FDF5E6",
    "#FFF5EE",
    "#FFFAFA",
    "#FFFFFF",
    "#F5F5F5",
]

DARK_COLORS = [
    "#000000",
    "#00008B",
    "#191970",
    "#483D8B",
    "#2F4F4F",
    "#4B0082",
    "#191970",
    "#000080",
]


# Taken from here:
# http://mkweb.bcgsc.ca/colorblind/palettes.mhtml
# http://mkweb.bcgsc.ca/colorblind/palettes/8.color.blindness.palette.txt
COLORBLIND8_COLORS = [
    "#000000",
    "#2271B2",
    "#3DB7E9",
    "#F748A5",
    "#359B73",
    "#d55e00",
    "#e69f00",
    "#f0e442",
]


# Taken from here:
# http://mkweb.bcgsc.ca/colorblind/palettes.mhtml
# http://mkweb.bcgsc.ca/colorblind/palettes/12.color.blindness.palette.txt
COLORBLIND12_COLORS = [
    "#9F0162",
    "#009F81",
    "#FF5AAF",
    "#00FCCF",
    "#8400CD",
    "#008DF9",
    "#00C2F9",
    "#FFB2FD",
    "#A40122",
    "#E20134",
    "#FF6E3A",
    "#FFC33B",
]


# Taken from here:
# http://mkweb.bcgsc.ca/colorblind/palettes.mhtml
# http://mkweb.bcgsc.ca/colorblind/palettes/15.color.blindness.palette.txt
COLORBLIND15_COLORS = [
    "#68023F",
    "#008169",
    "#EF0096",
    "#00DCB5",
    "#FFCFE2",
    "#003C86",
    "#9400E6",
    "#009FFA",
    "#FF71FD",
    "#7CFFFA",
    "#6A0213",
    "#008607",
    "#F60239",
    "#00E307",
    "#FFDC3D",
]


# Taken from here:
# http://mkweb.bcgsc.ca/colorblind/palettes.mhtml
# http://mkweb.bcgsc.ca/colorblind/palettes/24.color.blindness.palette.txt
COLORBLIND24_COLORS = [
    "#003D30",
    "#005745",
    "#00735C",
    "#009175",
    "#00AF8E",
    "#00CBA7",
    "#00EBC1",
    "#86FFDE",
    "#00306F",
    "#00489E",
    "#005FCC",
    "#0079FA",
    "#009FFA",
    "#00C2F9",
    "#00E5F8",
    "#7CFFFA",
    "#004002",
    "#005A01",
    "#007702",
    "#009503",
    "#00B408",
    "#00D302",
    "#00F407",
    "#AFFF2A",
]

COLOR_LIST_X11 = "x11"
COLOR_LIST_LIGHT = "light"
COLOR_LIST_DARK = "dark"
COLOR_LIST_COLORBLIND8 = "colorblind8"
COLOR_LIST_COLORBLIND12 = "colorblind12"
COLOR_LIST_COLORBLIND15 = "colorblind15"
COLOR_LIST_COLORBLIND24 = "colorblind24"
COLOR_LISTS = {
    COLOR_LIST_X11: X11_COLORS,
    COLOR_LIST_LIGHT: LIGHT_COLORS,
    COLOR_LIST_DARK: DARK_COLORS,
    COLOR_LIST_COLORBLIND8: COLORBLIND8_COLORS,
    COLOR_LIST_COLORBLIND12: COLORBLIND12_COLORS,
    COLOR_LIST_COLORBLIND15: COLORBLIND15_COLORS,
    COLOR_LIST_COLORBLIND24: COLORBLIND24_COLORS,
}


PALETTE_AUTO = "auto"
PALETTE_GRAYSCALE = "grayscale"
PALETTE_X11 = "x11"
PALETTE_LIGHT = "light"
PALETTE_DARK = "dark"
PALETTE_COLORBLIND8 = "colorblind8"
PALETTE_COLORBLIND12 = "colorblind12"
PALETTE_COLORBLIND15 = "colorblind15"
PALETTE_COLORBLIND24 = "colorblind24"
PALETTES = {
    PALETTE_AUTO: None,
    PALETTE_GRAYSCALE: None,
    PALETTE_X11: X11_COLORS,
    PALETTE_LIGHT: LIGHT_COLORS,
    PALETTE_DARK: DARK_COLORS,
    PALETTE_COLORBLIND8: COLORBLIND8_COLORS,
    PALETTE_COLORBLIND12: COLORBLIND12_COLORS,
    PALETTE_COLORBLIND15: COLORBLIND15_COLORS,
    PALETTE_COLORBLIND24: COLORBLIND24_COLORS,
}


def colors(color_list: str = COLOR_LIST_X11) -> List[Tuple[int, int, int]]:
    """
    Returns a list of color tuples from the specified colors list.

    :param color_list: the colors list to use (see COLOR_LISTS, default is COLOR_LIST_X11)
    :type color_list: str
    :return: the nested list of colors
    :rtype: list
    """
    if color_list not in COLOR_LISTS:
        raise Exception("Unknown color palette!")
    result = []
    for c in COLOR_LISTS[color_list]:
        result.append(ImageColor.getrgb(c))
    return result


def x11_colors(no_light: bool = True, no_dark: bool = True) -> List[Tuple[int, int, int]]:
    """
    Returns a list of color tuples from X11_COLORS.

    :param no_light: skips light colors
    :type no_light: bool
    :param no_dark: skips dark colors
    :type no_dark: bool
    :return: the nested list of colors
    :rtype: list
    """
    result = []
    skip = set()
    if no_light:
        for c in LIGHT_COLORS:
            skip.add(c)
    if no_dark:
        for c in DARK_COLORS:
            skip.add(c)
    for c in X11_COLORS:
        if c in skip:
            continue
        result.append(ImageColor.getrgb(c))
    return result


def grayscale_palette(num_colors: int) -> List[int]:
    """
    Returns a list of palette entries (R,G,B) with the specified number of grayscale colors.

    :param num_colors: the number of colors to generate
    :type num_colors: int
    :return: the generated list of colors
    :rtype: list
    """
    return [1 + i // 3 for i in range(3*num_colors)]


def fill_palette(palette_list: List[int]) -> List[int]:
    """
    Makes sure that there are 256 R,G,B values present. Simply adds grayscale R,G,B values.

    :param palette_list: the palette to fill up, if necessary
    :type palette_list: list
    :return: the (potentially) updated list of R,G,B values
    :rtype: list
    """
    if len(palette_list) < 256*3:
        if len(palette_list) % 3 != 0:
            raise ValueError("Palette does not contain multiples of three (ie R,G,B values)!")
        palette_list = palette_list + grayscale_palette(256 - (len(palette_list) // 3))
    return palette_list


def default_palette(palette: str = None) -> List[int]:
    """
    Returns a palette of 255 R,G,B triplets all in a single list, to be used in indexed PNG files.
    Black is always the first color.

    :return: the flat list of R,G,B values
    :rtype: list
    """
    if palette is None:
        palette = PALETTE_AUTO
    if palette not in PALETTES:
        raise ValueError("Unknown palette: %s" % palette)
    if palette == PALETTE_AUTO:
        # custom values?
        if PALETTES[PALETTE_AUTO] is not None:
            result = [0, 0, 0]
            for c in PALETTES[PALETTE_GRAYSCALE]:
                if c == "#000000":
                    continue
                result.extend(ImageColor.getrgb(c))
        else:
            result = [0, 0, 0,      # black
                      255, 0, 0,    # red
                      0, 255, 0,    # green
                      0, 0, 255,    # blue
                      255, 0, 255,  # magenta
                      255, 255, 0,  # yellow
                      0, 255, 255]  # cyan
    elif palette == PALETTE_GRAYSCALE:
        result = [0, 0, 0]
        # custom values?
        if PALETTES[PALETTE_GRAYSCALE] is not None:
            for c in PALETTES[PALETTE_GRAYSCALE]:
                if c == "#000000":
                    continue
                result.extend(ImageColor.getrgb(c))
        else:
            # fill_palette call further down fills in grayscale colors
            pass
    else:
        result = [0, 0, 0]
        for c in PALETTES[palette]:
            if c == "#000000":
                continue
            result.extend(ImageColor.getrgb(c))

    result = fill_palette(result)
    return result


def generate_palette_list(palette: str = None) -> List[int]:
    """
    Generates a flat integer list of RGB values from the palette name or the comma-separated list of RGB values.
    Ensures that there are 256 R,G,B values output when supplying comma-separated list of RGB values.

    :param palette: the palette name (uses PALETTE_AUTO if None) or the comma-separated list of RGB values
    :type palette: str
    :return: the list of RGB values for the palette
    """
    if palette is None:
        palette = PALETTE_AUTO
    if palette not in PALETTES:
        if "," in palette:
            result = [int(x) for x in palette.split(",")]
            result = fill_palette(result)
        else:
            raise Exception("Unknown palette: %s" % palette)
    else:
        result = default_palette(palette=palette)
    return result


def parse_rgb(color_list: List[str]) -> List[Tuple[int, int, int]]:
    """
    Parses the list of RGB triplets (separated by comma) into a list of triplet integers.

    :param color_list: the list of colors to parse
    :type color_list: list
    :return: the list of R,G,B tuples
    :rtype: list
    """
    result = []
    if color_list is not None:
        for color in color_list:
            if "," in color:
                rgb = [int(x) for x in color.split(",")]
                if len(rgb) == 3:
                    result.append((rgb[0], rgb[1], rgb[2]))
    return result


def parse_rgba(color_list: List[str]) -> List[Tuple[int, int, int, int]]:
    """
    Parses the list of RGBA quadruplets (separated by comma) into a list of quadruplet integers.

    :param color_list: the list of colors to parse
    :type color_list: list
    :return: the list of R,G,B,A tuples
    :rtype: list
    """
    result = []
    if color_list is not None:
        for color in color_list:
            if "," in color:
                rgb = [int(x) for x in color.split(",")]
                if len(rgb) == 4:
                    result.append((rgb[0], rgb[1], rgb[2], rgb[3]))
    return result


def palettes() -> List[str]:
    """
    Returns the sorted list of palette names.

    :return: the list of names
    :rtype: list
    """
    return sorted(PALETTES.keys())


def color_lists() -> List[str]:
    """
    Returns the sorted list of color list names.

    :return: the list of names
    :rtype: list
    """
    return sorted(COLOR_LISTS.keys())


class ColorProvider:
    """
    Generates RGB triplets of RGBA quadruplets from a predefined colors or custom colors.
    If the color_list is COLOR_LIST_X11, then no dark and no light colors will be used.
    """

    def __init__(self, color_list: str = COLOR_LIST_X11, custom_colors: List[Tuple[int, int, int]] = None,
                 label_mapping: Dict = None):
        """
        Initializes the color provider.

        :param color_list: the name of the color list with the default colors to use
        :type color_list: str
        :param custom_colors: the list of custom colors to use
        :type custom_colors: list
        """
        if color_list not in COLOR_LISTS:
            raise Exception("Unknown color list '%s'! Available lists: %s" % (color_list, color_lists()))
        self._colors = dict()
        if color_list == COLOR_LIST_X11:
            self._default_colors = x11_colors()  # no dark, no light
        else:
            self._default_colors = colors(color_list)
        self._default_colors_index = 0
        self._custom_colors = custom_colors
        if self._custom_colors is None:
            self._custom_colors = []
        self._label_mapping = label_mapping
        if self._label_mapping is None:
            self._label_mapping = dict()

    @property
    def label_mapping(self) -> Dict:
        """
        Returns the current label mapping (label/index).

        :return: the label mapping
        :rtype: dict
        """
        return self._label_mapping

    @label_mapping.setter
    def label_mapping(self, mapping: Dict):
        """
        Sets the new label mapping to use (label/index).

        :param mapping: the label mapping
        :type mapping: dict
        """
        self._label_mapping = mapping

    def _next_default_color(self) -> Tuple[int, int, int]:
        """
        Returns the next default color.

        :return: the RGB color tuple
        :rtype: tuple
        """
        if self._default_colors_index >= len(self._default_colors):
            self._default_colors_index = 0
        result = self._default_colors[self._default_colors_index]
        self._default_colors_index += 1
        return result

    def get_color(self, label: str, alpha: int = None) -> Union[Tuple[int, int, int], Tuple[int, int, int, int]]:
        """
        Returns the color for the label.

        :param label: the label to get the color for
        :type label: str
        :param alpha: the alpha value to use, ignored if None
        :type alpha: int or None
        :return: the RGB or RGBA color tuple
        :rtype: tuple
        """
        if label not in self._colors:
            has_custom = False
            if label in self._label_mapping:
                index = self._label_mapping[label]
                if index < len(self._custom_colors):
                    has_custom = True
                    self._colors[label] = self._custom_colors[index]
            if not has_custom:
                self._colors[label] = self._next_default_color()
        r, g, b = self._colors[label]
        if alpha is None:
            return r, g, b
        else:
            return r, g, b, alpha


def add_color_list(name: str, values: List[str]):
    """
    Adds the color list value under the specified name.

    :param name: the name of the color list
    :type name: str
    :param values: the list of hex colors values associated with the name
    :type values: list
    """
    global COLOR_LISTS
    COLOR_LISTS[name] = values


def add_palette(name: str, values: List[str]):
    """
    Adds the color list value under the specified name.

    :param name: the name of the color list
    :type name: str
    :param values: the list of hex colors values associated with the name
    :type values: list
    """
    global PALETTES
    PALETTES[name] = values


def palette_list_to_triplets(palette: List[int]) -> List[Tuple[int, int, int]]:
    """
    Turns a palette list into a list of R,G,B triplets.

    :param palette: the list to convert
    :type palette: list
    :return: the list of R,G,B tuples
    :rtype: list
    """
    if len(palette) % 3 != 0:
        raise Exception("Palette list must have length that is divisible by three, but got: %d" % len(palette))
    result = []
    for i in range(0, len(palette), 3):
        result.append((palette[i], palette[i+1], palette[i+2]))
    return result
