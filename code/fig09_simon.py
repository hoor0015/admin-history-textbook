# 9주차 2차시 그림: 사이먼이 드러낸 상충하는 원리의 쌍들
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


# ---------------------------------------------------------------- 그림 9-2
# 상충하는 원리 쌍 비교도
fig, ax = plt.subplots(figsize=(11, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 13)
ax.axis("off")

pairs = [
    (10.6, "전문화의 원리\n각 결정은 가장 전문적으로\n내릴 수 있는 지점에서",
     "명령통일의 원리\n명령은 오직 한 사람의\n상관에게서만"),
    (8.2, "통솔범위의 원리\n한 관리자가 감독하는\n부하의 수를 줄여라",
     "단계 최소화의 격언\n사안이 거치는 조직\n단계의 수를 줄여라"),
    (5.8, "목적에 따른 편성\n같은 서비스를 좇는 사람들을\n한 부서로",
     "과정·고객·지역에 따른 편성\n같은 기술·대상·구역의 사람들을\n한 부서로"),
]
for y, left, right in pairs:
    box(ax, 0.5, y, 5.0, 1.8, left, fc="#f5f9fd", ec="#2f6fb0", fontsize=10)
    box(ax, 8.5, y, 5.0, 1.8, right, fc="#fdf9f4", ec="#c77b2f", fontsize=10)
    arrow(ax, 5.7, y + 0.9, 6.5, y + 0.9, style="-", color="#b03a3a", lw=2.0)
    arrow(ax, 8.3, y + 0.9, 7.5, y + 0.9, style="-", color="#b03a3a", lw=2.0)
    ax.text(7.0, y + 0.9, "충돌", ha="center", va="center", fontsize=11,
            color="#b03a3a", fontweight="bold",
            bbox=dict(fc="white", ec="#b03a3a", boxstyle="round,pad=0.3"))

box(ax, 2.5, 3.2, 9.0, 1.5,
    "사이먼의 진단: 두 원리는 정확히 반대되는 처방으로 이끄는데,\n이론에는 어느 쪽을 적용해야 옳은지 가리키는 것이 없다 (원리는 격언이다)",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=10.5, weight="bold")
arrow(ax, 7.0, 5.6, 7.0, 4.9)

box(ax, 2.5, 0.7, 9.0, 1.5,
    "사이먼의 처방: 원리를 조직 진단의 '기준'으로 강등하고,\n상충하는 기준들의 적용 조건과 가중치를 경험 연구로 밝힌다",
    fc="#faf8fc", ec="#7a5fa8", fontsize=10.5)
arrow(ax, 7.0, 3.1, 7.0, 2.4)

ax.set_title("사이먼이 드러낸 상충하는 원리의 쌍들 (「행정의 격언들」, 1946)", fontsize=13, pad=14)

fig.tight_layout()
fig.savefig(FIG / "fig09_conflicting_principles.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("saved:", FIG / "fig09_conflicting_principles.png")
