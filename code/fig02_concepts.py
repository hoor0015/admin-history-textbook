# 2주차 개념도 생성 (그림 2-1 유교 통치론 구조도, 그림 2-2 키케로 생애 연표)
# 실행: cd ~/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401

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


# ---------------------------------------------------------------- 그림 2-1
# 유교 통치론의 구조: 수신에서 평천하까지, 그리고 논어의 근거 구절
fig, ax = plt.subplots(figsize=(11.5, 6.0))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis("off")

ax.text(6.5, 8.55, "통치의 출발점은 제도가 아니라 통치자 자신이다",
        ha="center", fontsize=12.5, fontweight="bold", color="#333")

stages = [
    ("수신(修身)\n자기를 바르게 닦는다", "#fbf8f2", "#8a6d3b"),
    ("제가(齊家)\n집안을 가지런히 한다", "#f5f9fd", "#2f6fb0"),
    ("치국(治國)\n나라를 다스린다", "#f5f9fd", "#2f6fb0"),
    ("평천하(平天下)\n천하를 평안하게 한다", "#faf8fc", "#7a5fa8"),
]
for i, (t, fc, ec) in enumerate(stages):
    x = 0.5 + i * 3.2
    box(ax, x, 5.6, 2.7, 1.8, t, fc=fc, ec=ec, fontsize=11,
        weight="bold" if i == 0 else "normal")
    if i < 3:
        arrow(ax, x + 2.85, 6.5, x + 3.15, 6.5)
ax.text(6.5, 7.9, "유교 경전 『대학』이 정리한 통치의 단계: 안에서 밖으로 확장된다",
        ha="center", fontsize=10, color="#555")

quotes = [
    (0.5, "其身正, 不令而行\n자기가 바르면 명령하지\n않아도 행해진다 (자로 6)", 1.85),
    (4.9, "政者, 正也\n정치란 바르게 하는\n것이다 (안연 17)", 6.25),
    (9.3, "君子之德風, 小人之德草\n군자의 덕은 바람, 백성의\n덕은 풀이다 (안연 19)", 10.65),
]
for x, t, ax_x in quotes:
    box(ax, x, 2.4, 3.2, 2.0, t, fc="#fbf8f2", ec="#8a6d3b", fontsize=9.5)
arrow(ax, 2.1, 4.55, 1.9, 5.5, color="#8a6d3b")
arrow(ax, 6.5, 4.55, 7.2, 5.5, color="#8a6d3b")
arrow(ax, 10.9, 4.55, 10.6, 5.5, color="#8a6d3b")
ax.text(6.5, 1.2, "『논어』의 정치 문답이 각 단계를 뒷받침한다.\n"
                  "통치자의 덕이 바람처럼 백성에게 미친다는 것이 덕치(德治)의 논리다.",
        ha="center", fontsize=10.5, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.5"))
fig.savefig(FIG / "fig02_confucius.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 2-2
# 키케로의 생애와 로마 공화정 말기 연표
fig, ax = plt.subplots(figsize=(12, 5.6))
ax.set_xlim(148, 13)  # 기원전 연도: 왼쪽이 과거
ax.set_ylim(-5.2, 5.4)
ax.axis("off")

# 기준선
arrow(ax, 146, 0, 15, 0, color="#888", lw=2.0)
for year in [130, 110, 90, 70, 50, 30]:
    ax.plot([year, year], [-0.18, 0.18], color="#888", lw=1.2)
    ax.text(year, -0.75, f"BC {year}", ha="center", fontsize=9, color="#666")

# 위: 키케로의 생애 (주황)
life = [
    (106, "출생\n(아르피눔, 기사 계급)", 1.5),
    (75, "재무관\n(관직 진출)", 3.2),
    (63, "집정관\n카틸리나 음모 진압", 1.5),
    (57, "망명(BC 58)에서\n귀환, 저술 전념", 4.4),
    (44, "『의무론』 집필", 1.7),
    (43, "안토니우스의 명령으로\n피살(포르미아)", 3.1),
]
for year, label, h in life:
    ax.plot([year, year], [0, h - 0.55], color="#c77b2f", lw=1.2, ls="--")
    ax.text(year, h, label, ha="center", va="center", fontsize=9.2, color="#7a4a15",
            bbox=dict(fc="#fdf9f4", ec="#c77b2f", boxstyle="round,pad=0.35", lw=1.2))

# 아래: 공화정 말기의 사건 (파랑)
events = [
    (133, "그라쿠스 형제의 개혁과\n죽음(BC 133-121): 위기의 시작", -1.9),
    (60, "제1차 삼두정치\n(카이사르·폼페이우스·크라수스)", -3.7),
    (49, "카이사르 내전 시작", -1.9),
    (44, "카이사르 암살", -3.0),
    (27, "아우구스투스 제정 수립\n(공화정의 종언)", -1.9),
]
for year, label, h in events:
    ax.plot([year, year], [0, h + 0.55], color="#2f6fb0", lw=1.2, ls="--")
    ax.text(year, h, label, ha="center", va="center", fontsize=9.2, color="#1d4671",
            bbox=dict(fc="#f5f9fd", ec="#2f6fb0", boxstyle="round,pad=0.35", lw=1.2))

ax.text(146, 4.9, "위: 키케로의 생애", fontsize=10.5, color="#7a4a15",
        fontweight="bold", ha="left")
ax.text(146, -4.8, "아래: 로마 공화정 말기의 사건", fontsize=10.5, color="#1d4671",
        fontweight="bold", ha="left")
fig.savefig(FIG / "fig02_cicero.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig02_*.png'))])
