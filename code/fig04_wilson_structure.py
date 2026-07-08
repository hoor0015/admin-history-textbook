# 4주차 2차시 그림 4-2: 윌슨 「행정학 연구」(1887)의 구조
# 실행: cd ~/default-uv-env && PYTHONIOENCODING=utf-8 VIRTUAL_ENV= uv run python "<이 파일 경로>"
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")
import koreanize_matplotlib  # noqa: E402,F401

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

FIG = Path(__file__).resolve().parent.parent / "figures"
FIG.mkdir(exist_ok=True)


def box(ax, x, y, w, h, text, fc="#f5f9fd", ec="#2f6fb0", fontsize=10, weight="normal"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.08",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            fontsize=fontsize, fontweight=weight)


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.6, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, color=color, lw=lw, linestyle=ls))


fig, ax = plt.subplots(figsize=(12, 6.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")

# 맨 위: 출발점 (행정 연구의 두 목적)
box(ax, 2.6, 8.0, 6.8, 1.7,
    "행정 연구의 두 가지 목적\n① 정부가 마땅히 잘할 수 있는 일은 무엇인가\n② 그 일을 최고의 효율·최소의 비용으로 하는 방법은 무엇인가",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=10, weight="bold")

# 아래 세 상자: 논문의 세 부분
box(ax, 0.4, 3.6, 3.4, 3.2,
    "제1부 연구의 역사\n\n왜 이제야 연구하는가\n· 2,200년 늦은 열매\n· \"누가 법을 만들 것인가\"\n에 밀려난 집행\n· 복잡해진 정부\n· 민주정의 어려움",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=9.5)
box(ax, 4.3, 3.6, 3.4, 3.2,
    "제2부 연구의 대상\n\n행정의 영역은 무엇인가\n· 행정은 정치 바깥의\n\"사업\"의 영역\n· 정치-행정의 구분\n· 여론의 역할",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=9.5)
box(ax, 8.2, 3.6, 3.4, 3.2,
    "제3부 연구의 방법\n\n어떻게 연구하는가\n· 역사적·비교 연구\n· 유럽 모델에서 배우기\n· 원리의 \"미국화\"",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=9.5)

arrow(ax, 4.5, 7.9, 2.1, 6.9)
arrow(ax, 6.0, 7.9, 6.0, 6.9)
arrow(ax, 7.5, 7.9, 9.9, 6.9)

# 아래: 주차 배분 표시
box(ax, 0.4, 1.0, 3.4, 1.6, "이번 차시에서 읽는 부분\n(4주차 2차시)",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=10, weight="bold")
box(ax, 4.3, 1.0, 7.3, 1.6, "다음 주에 읽는 부분 (5주차 1차시)\n정치-행정 이원론과 유럽 모델의 미국화",
    fc="#fdf9f4", ec="#c77b2f", fontsize=10, weight="bold")
arrow(ax, 2.1, 3.5, 2.1, 2.7, color="#2f8f4e")
arrow(ax, 6.0, 3.5, 6.0, 2.7, color="#c77b2f")
arrow(ax, 9.9, 3.5, 9.9, 2.7, color="#c77b2f")

fig.tight_layout()
fig.savefig(FIG / "fig04_wilson_structure.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("saved:", FIG / "fig04_wilson_structure.png")
