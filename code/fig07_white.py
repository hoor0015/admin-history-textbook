# 7주차 2차시 개념도 생성 (화이트: 행정학 제도화 연표, 네 가지 가정)
# 실행: cd ~/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401
import figfit  # noqa: E402,F401  (상자 글씨 자동 크기)

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(exist_ok=True)


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec="#2f6fb0", fontsize=11, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


# ---------------------------------------------------------------- 그림 7-3
# 행정학 제도화의 연표 1887-1926
fig, ax = plt.subplots(figsize=(12, 5.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

ax.plot([0.6, 11.4], [4.0, 4.0], color="#999", lw=2, zorder=1)
arrow(ax, 11.0, 4.0, 11.5, 4.0, color="#999", lw=2)

events = [
    (1887, "윌슨\n「행정학 연구」\n행정 연구의 촉구", "#f5f9fd", "#2f6fb0", "up"),
    (1900, "굿나우\n『정치와 행정』\n이원론의 정교화", "#f4fbf6", "#2f8f4e", "down"),
    (1911, "테일러\n『과학적 관리의 원칙』\n능률의 복음", "#faf8fc", "#7a5fa8", "up"),
    (1922, "베버 「관료제」\n사후 출판\n(영역은 1946)", "#fdf9f4", "#c77b2f", "down"),
    (1926, "화이트\n『행정학 입문』\n최초의 교과서", "#fbf8f2", "#8a6d3b", "up"),
]
x0, x1, y0, y1 = 1887, 1926, 1.1, 10.9


def xpos(year):
    return 1.7 + (year - x0) / (x1 - x0) * 8.8


for year, label, fc, ec, pos in events:
    x = xpos(year)
    ax.plot([x], [4.0], marker="o", color=ec, markersize=7, zorder=3)
    if pos == "up":
        box(ax, x - 1.35, 5.3, 2.7, 1.9, label, fc=fc, ec=ec, fontsize=9.5)
        ax.plot([x, x], [4.1, 5.25], color=ec, lw=1.2, ls=":")
        ax.text(x, 3.5, str(year), ha="center", fontsize=11, fontweight="bold", color="#333")
    else:
        box(ax, x - 1.35, 1.0, 2.7, 1.9, label, fc=fc, ec=ec, fontsize=9.5)
        ax.plot([x, x], [2.95, 3.9], color=ec, lw=1.2, ls=":")
        ax.text(x, 4.4, str(year), ha="center", fontsize=11, fontweight="bold", color="#333")

ax.text(6.0, 7.7, "정당화(윌슨) → 영역 구분(굿나우) → 방법의 모범(테일러) → 이론적 뼈대(베버) → 체계화(화이트)",
        ha="center", fontsize=10.5, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.5"))
fig.savefig(FIG / "fig07_white_timeline.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-4
# 화이트의 네 가지 가정과 관리 중심 행정학
fig, ax = plt.subplots(figsize=(12, 5.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

assumptions = [
    "가정 1. 행정은 단일한 과정이다\n(시·주·연방에 공통)",
    "가정 2. 연구의 토대는\n법이 아니라 관리다",
    "가정 3. 행정은 아직 예술이지만\n과학으로 전환될 수 있다",
    "가정 4. 행정은 현대 정부\n문제의 핵심이다",
]
ys = [6.2, 4.5, 2.8, 1.1]
for t, y in zip(assumptions, ys):
    box(ax, 0.5, y, 4.6, 1.4, t, fc="#f5f9fd", ec="#2f6fb0", fontsize=10)
    arrow(ax, 5.2, y + 0.7, 6.6, 4.0, color="#888")

box(ax, 6.8, 2.6, 4.6, 2.8,
    "관리 중심 행정학의 성립\n\n하나의 행정학, 하나의 교과서\n조직·인사·재무 등 관리 기능 중심\n'예술에서 과학으로'라는 이상",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=10.5, weight="bold")
ax.text(9.1, 1.3, "오늘날 행정학 커리큘럼의 원형", ha="center", fontsize=10, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.4"))
arrow(ax, 9.1, 2.5, 9.1, 1.8, color="#8a6d3b")
fig.savefig(FIG / "fig07_white_assumptions.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig07_*.png'))])
