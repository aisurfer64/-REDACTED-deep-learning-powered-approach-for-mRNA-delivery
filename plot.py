"""MIT License

Copyright (c) 2025 Aditya Gopu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

from typing import Iterable
import numpy as np
import skunk
from matplotlib.offsetbox import AnnotationBbox, OffsetImage, TextArea, VPacker


def _nearest_spiral_layout(x, y, offset):
    # make spiral
    angles = np.linspace(-np.pi, np.pi, len(x) + 1 + offset)[offset:]
    coords = np.stack((np.cos(angles), np.sin(angles)), -1)
    order = np.argsort(np.arctan2(y, x))
    return coords[order]


def _image_scatter(x, y, imgs, subtitles, colors, ax, offset=0):
    if isinstance(offset, int):
        box_coords = _nearest_spiral_layout(x, y, offset)
    elif isinstance(offset, Iterable) and len(offset) == 2:
        box_coords = offset
    bbs = []
    for i, (x0, y0, im, t, c) in enumerate(zip(x, y, imgs, subtitles, colors)):
        # TODO Figure out how to put this back
        # im = trim(im)
        img_data = np.asarray(im)
        img_box = skunk.ImageBox(f"rdkit-img-{i}", img_data)
        title_box = TextArea(t)
        packed = VPacker(children=[img_box, title_box], pad=0, sep=4, align="center")
        bb = AnnotationBbox(
            packed,
            (x0, y0),
            frameon=True,
            xybox=box_coords[i] + 0.5 if isinstance(offset, int) else offset,
            arrowprops=dict(arrowstyle="->", edgecolor="black"),
            pad=0.3,
            boxcoords="axes fraction",
            bboxprops=dict(edgecolor=c),
        )
        ax.add_artist(bb)

        bbs.append(bb)
    return bbs

# custom colormap
facecolors_customize = [
    "#a6d9daff",
    "#96c9ccff",
    "#91bfc2ff",
    "#8cb7baff",
    "#8aafb2ff",
    "#87a5aaff",
    "#849d9fff",
    "#829495ff",
    "#829091ff",
    "#828c8bff",
    "#828486ff",
    "#828282ff",
    "#807a7dff",
    "#79727aff",
    "#726674ff",
    "#6a596fff",
    "#624e67ff",
    "#5a4261ff",
    "#513957ff",
    "#492f4fff",
    "#40263eff",
    "#39233fff",
    "#32203fff",
]
