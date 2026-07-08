# 10주차 2차시 개념도 생성 (왈도, 행정국가 다시 보기 II)
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


# ---------------------------------------------------------------- 그림 10-3
# 정통 교리의 네 전제와 왈도의 해부
fig, ax = plt.subplots(figsize=(11.5, 5.8))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9.5)
ax.axis("off")

ax.text(6.5, 9.1, "행정학 정통 교리의 네 전제 (왈도의 정리)",
        ha="center", fontsize=12.5, fontweight="bold")

items = [
    ("① 과학이 가능하다\n행정에 관한 과학을\n세울 수 있다는 전제", "#f5f9fd", "#2f6fb0"),
    ("② 원리를 성취할 수 있다\n보편적 행정 '원리'가\n존재한다는 전제", "#f4fbf6", "#2f8f4e"),
    ("③ 세계는 둘로 나뉜다\n정치와 행정이라는\n두 영역의 구분", "#faf8fc", "#7a5fa8"),
    ("④ 능률이 기준이다\n행정을 재는 잣대는\n능률이라는 전제", "#fdf9f4", "#c77b2f"),
]
for i, (t, fc, ec) in enumerate(items):
    x = 0.5 + i * 3.1
    box(ax, x, 5.6, 2.8, 2.6, t, fc=fc, ec=ec, fontsize=10)
    cx = x + 1.4
    arrow(ax, cx, 5.5, cx + (6.5 - cx) * 0.4, 4.7, color="#999", lw=1.2)

box(ax, 3.4, 3.0, 6.2, 1.6,
    "정통 교리: 사실의 언어로 말하지만 실은 하나의 정치이론",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=11, weight="bold")

box(ax, 0.8, 0.4, 5.4, 1.8,
    "왈도의 해부 (『행정국가』 1948)\n전제 하나하나가 시대의 산물이며\n검토와 비판의 대상이라고 선언",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=10.5)
box(ax, 6.9, 0.4, 5.4, 1.8,
    "사이먼에 대한 왈도의 평가 (1965)\n네 전제를 재구성했지만 그대로 계승,\n곧 '새로운 포장에 담긴 옛 상품'",
    fc="#fdf9f4", ec="#c77b2f", fontsize=10.5)
arrow(ax, 5.4, 2.9, 4.2, 2.3)
arrow(ax, 7.6, 2.9, 8.8, 2.3)
fig.tight_layout()
fig.savefig(FIG / "fig10_orthodoxy.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 10-4
# 능률 대 민주주의: 왈도-사이먼 논쟁 구도
fig, ax = plt.subplots(figsize=(11.5, 6.4))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10.5)
ax.axis("off")

box(ax, 3.4, 8.6, 6.2, 1.4, "행정을 어떻게 이해할 것인가\n과학인가 정치인가, 사실인가 가치인가",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=11, weight="bold")
arrow(ax, 5.2, 8.5, 3.4, 7.5)
arrow(ax, 7.8, 8.5, 9.6, 7.5)

box(ax, 0.6, 3.4, 5.3, 4.0,
    "허버트 사이먼\n(『행정행태』 1947)\n\n사실과 가치의 엄격한 구분\n행정과학은 사실의 영역에서 가능\n판단 기준은 능률\n철학적 기초는 논리실증주의",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5)
box(ax, 7.1, 3.4, 5.3, 4.0,
    "드와이트 왈도\n(『행정국가』 1948)\n\n행정이론은 곧 정치이론\n행정가는 가치판단을 피할 수 없음\n판단 기준은 민주주의\n능률 자체가 이미 하나의 가치",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=10.5)

arrow(ax, 5.95, 5.4, 7.05, 5.4, style="<|-|>", color="#c0392b", lw=2.0)
ax.text(6.5, 6.0, "왈도-사이먼 논쟁\n(1952, APSR)", ha="center", fontsize=10,
        color="#c0392b", fontweight="bold")

box(ax, 2.2, 0.5, 8.6, 1.9,
    "능률과 민주주의의 긴장은 해소되지 않은 채 남는다\n왈도의 물음은 1968년 미노브룩 회의와 신행정학으로 이어진다 (11주차)",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=11, weight="bold")
arrow(ax, 3.2, 3.3, 4.6, 2.5)
arrow(ax, 9.8, 3.3, 8.4, 2.5)
fig.tight_layout()
fig.savefig(FIG / "fig10_tension.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig10_*.png'))])
