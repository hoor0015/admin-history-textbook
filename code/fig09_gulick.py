# 9주차 2차시 개념도 생성 (귤릭: 조직이론과 POSDCORB)
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


# ---------------------------------------------------------------- 그림 9-3
# 분업과 조정의 두 경로
fig, ax = plt.subplots(figsize=(11, 6.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 3.7, 8.2, 4.6, 1.5, "분업(전문화)\n조직이 존재하는 이유", fc="#fdf9f4", ec="#c77b2f", weight="bold")
box(ax, 3.7, 5.8, 4.6, 1.3, "나뉜 일은 다시 묶어야 한다\n조정(co-ordination)의 필요", fc="#fbf8f2", ec="#8a6d3b")
arrow(ax, 6.0, 8.1, 6.0, 7.25)

box(ax, 0.6, 2.4, 4.9, 2.5,
    "조직에 의한 조정\n권한의 구조와 명령 체계\n설계 원리: 통솔범위,\n명령 일원화, 동질성",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5)
box(ax, 6.5, 2.4, 4.9, 2.5,
    "아이디어의 지배에 의한 조정\n공동 목적에 대한 일체감\n각자가 자발적으로 자기 일을\n전체에 끼워 맞춘다",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=10.5)
arrow(ax, 5.2, 5.7, 3.4, 5.05)
arrow(ax, 6.8, 5.7, 8.6, 5.05)

ax.text(6.0, 1.1, "두 경로는 배타적이지 않다. 둘을 폭넓게 함께 쓰지 않는 사업은 효과적일 수 없다.",
        ha="center", fontsize=11, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.5"))
ax.set_title("분업은 조정을 부른다: 귤릭이 본 조정의 두 경로", fontsize=13, pad=10)
fig.savefig(FIG / "fig09_coordination.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 9-4
# POSDCORB 구조도
fig, ax = plt.subplots(figsize=(12.5, 5.0))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis("off")

box(ax, 4.6, 6.0, 4.8, 1.6, "최고책임자(chief executive)는\n무슨 일을 하는가?", fc="#fdf9f4", ec="#c77b2f", weight="bold")

items = [
    ("P", "기획\nPlanning", "#f5f9fd", "#2f6fb0"),
    ("O", "조직화\nOrganizing", "#f5f9fd", "#2f6fb0"),
    ("S", "인사\nStaffing", "#f5f9fd", "#2f6fb0"),
    ("D", "지휘\nDirecting", "#f4fbf6", "#2f8f4e"),
    ("Co", "조정\nCo-ordinating", "#f4fbf6", "#2f8f4e"),
    ("R", "보고\nReporting", "#faf8fc", "#7a5fa8"),
    ("B", "예산\nBudgeting", "#faf8fc", "#7a5fa8"),
]
BW, BH = 1.58, 2.2
for i, (abbr, label, fc, ec) in enumerate(items):
    x = 0.5 + i * 1.9
    box(ax, x, 1.4, BW, BH, f"{abbr}\n{label}", fc=fc, ec=ec, fontsize=10)
    arrow(ax, 7.0, 5.9, x + BW / 2, 3.8, color="#888", lw=1.2)

ax.text(7.0, 0.5, "일곱 요소는 페욜의 기능 분석을 토대로 한 것으로, 규모가 큰 조직에서는 각각을 집행부 안의 하위 부문으로 조직할 수 있다.",
        ha="center", fontsize=10.5, color="#333")
ax.set_title("POSDCORB: 최고책임자 기능의 일곱 요소", fontsize=13, pad=10)
fig.savefig(FIG / "fig09_posdcorb.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig09_*.png'))])
