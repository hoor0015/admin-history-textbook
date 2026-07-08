# 6주차 2차시 개념도 생성 (그림 6-3 과학적 관리 4원칙, 그림 6-4 유일 최선의 방법)
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


# ---------------------------------------------------------------- 그림 6-3
# 과학적 관리의 4원칙 구조도
fig, ax = plt.subplots(figsize=(11.5, 7.0))
ax.set_xlim(0, 13)
ax.set_ylim(0, 11)
ax.axis("off")

box(ax, 3.25, 9.2, 6.5, 1.4, "경영이 스스로 떠맡는 새로운 의무\n(테일러, 하원 특별위원회 증언, 1912)",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=11.5, weight="bold")

cells = [
    ("① 지식의 과학화\n노동자의 머릿속 경험 지식을\n수집·기록하여 법칙·규칙·\n공식으로 만든다", "#f5f9fd", "#2f6fb0"),
    ("② 과학적 선발과 발전\n성격·성향·성과를 연구해\n알맞은 일에 배치하고\n훈련시켜 승진시킨다", "#f4fbf6", "#2f8f4e"),
    ("③ 과학과 노동자의 결합\n만들어 둔 표준이 현장에서\n실제로 적용되도록\n곁에서 끌어낸다", "#faf8fc", "#7a5fa8"),
    ("④ 작업과 책임의 분담\n일을 경영과 노동이 나눈다\n(노동자 세 명마다\n경영 측 한 명)", "#fdf9f4", "#c77b2f"),
]
for i, (t, fc, ec) in enumerate(cells):
    x = 0.35 + i * 3.2
    box(ax, x, 5.0, 2.9, 3.0, t, fc=fc, ec=ec, fontsize=9.8)
    arrow(ax, 6.5, 9.1, x + 1.45, 8.3)

box(ax, 2.75, 1.2, 7.5, 2.2,
    "결과\n더 많은 산출, 더 높은 임금, 더 큰 이윤\n\"불화가 아니라 조화가 규칙인 관리\"",
    fc="white", ec="#8a6d3b", fontsize=11, weight="bold")
for i in range(4):
    x = 0.35 + i * 3.2 + 1.45
    arrow(ax, x, 4.9, 6.5, 3.6, color="#888")
fig.tight_layout()
fig.savefig(FIG / "fig06_taylor_principles.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 6-4
# 시간·동작 연구와 유일 최선의 방법
fig, ax = plt.subplots(figsize=(11.5, 5.6))
ax.set_xlim(0, 13)
ax.set_ylim(0, 8.5)
ax.axis("off")

box(ax, 0.4, 5.4, 3.4, 2.0, "시간 연구\n스톱워치로 작업을 반복\n측정해 표준 시간 산출", fc="#f5f9fd", ec="#2f6fb0", fontsize=10)
box(ax, 0.4, 2.4, 3.4, 2.0, "동작 연구\n동작을 최소 단위로 쪼개\n불필요한 움직임 제거", fc="#f4fbf6", ec="#2f8f4e", fontsize=10)
box(ax, 5.0, 3.9, 3.2, 2.0, "유일 최선의 방법\n(one best way)", fc="#fbf8f2", ec="#8a6d3b", fontsize=11.5, weight="bold")
arrow(ax, 3.9, 6.2, 5.2, 5.4)
arrow(ax, 3.9, 3.4, 5.2, 4.4)
box(ax, 9.4, 5.4, 3.2, 2.0, "표준화와 훈련\n모든 노동자에게 적용", fc="#faf8fc", ec="#7a5fa8", fontsize=10)
box(ax, 9.4, 2.4, 3.2, 2.0, "약속된 결과\n생산성 상승, 피로 감소,\n더 높은 임금", fc="#fdf9f4", ec="#c77b2f", fontsize=10)
arrow(ax, 8.3, 5.3, 9.6, 6.0)
arrow(ax, 11.0, 5.3, 11.0, 4.5)
ax.text(6.6, 1.0, "전제: 어떤 과업이든 그것을 수행하는 가장 좋은 한 가지 방법이 존재한다",
        ha="center", fontsize=11, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.5"))
fig.tight_layout()
fig.savefig(FIG / "fig06_one_best_way.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig06_*.png'))])
