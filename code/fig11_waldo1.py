# 11주차 1차시 개념도 생성 (왈도, 행정국가 다시 보기 I)
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


# ---------------------------------------------------------------- 그림 11-1
# 왈도의 작업 구도: 정치이론의 렌즈로 행정학 읽기
fig, ax = plt.subplots(figsize=(11, 5.6))
ax.set_xlim(0, 13)
ax.set_ylim(0, 9)
ax.axis("off")

box(ax, 0.5, 6.6, 5.6, 1.9,
    "최초의 문제의식 (1942년 박사논문 구상)\n민주주의 전통에서 '전문성'을 근거로 한\n권력 주장을 어떻게 받아들일 것인가",
    fc="#fdf9f4", ec="#c77b2f", fontsize=10.5)
box(ax, 7.4, 6.6, 5.1, 1.9,
    "대상의 축소\n거대한 설계 가운데 한 장(章),\n곧 행정학 문헌만 다루기로 결정",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=10.5)
arrow(ax, 6.2, 7.55, 7.3, 7.55)

box(ax, 7.4, 3.6, 5.1, 1.9,
    "방법: 정치이론의 렌즈\n'사실'과 '과학'을 말한다고 자처하는\n행정학 문헌을 정치이론으로 읽는다",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5, weight="bold")
arrow(ax, 9.95, 6.5, 9.95, 5.7)

box(ax, 0.5, 3.6, 5.6, 1.9,
    "발견\n행정학 밑에는 정치이론이라는\n기반(matrix)이 숨어 있다",
    fc="#faf8fc", ec="#7a5fa8", fontsize=10.5)
arrow(ax, 7.3, 4.55, 6.2, 4.55)

box(ax, 2.9, 0.6, 7.2, 1.9,
    "『행정국가』 (1948)\n행정학의 정통 교리를 하나의 정치이론으로 펼쳐 놓고\n정치이론가의 방식으로 검토하고 비판한다",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=11, weight="bold")
arrow(ax, 3.3, 3.5, 4.8, 2.7)

ax.text(11.6, 2.2, "저자들은 사실을\n말한다고 믿었지만,\n왈도는 그 밑의\n이론을 읽었다.",
        ha="center", fontsize=10, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.5"))
fig.tight_layout()
fig.savefig(FIG / "fig11_lens.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 11-2
# 행정학 정통 교리의 토양: 물질적 배경, 이념적 배경, 개혁운동
fig, ax = plt.subplots(figsize=(11.5, 6.2))
ax.set_xlim(0, 13)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 0.5, 8.1, 3.7, 1.2, "물질적 배경", fc="#f5f9fd", ec="#2f6fb0", fontsize=12, weight="bold")
box(ax, 0.5, 4.0, 3.7, 3.8,
    "도시화\n기업문명\n산업혁명과 기술 발전\n전문화의 진전",
    fc="white", ec="#2f6fb0", fontsize=10.5)

box(ax, 4.65, 8.1, 3.7, 1.2, "이념적 배경", fc="#faf8fc", ec="#7a5fa8", fontsize=12, weight="bold")
box(ax, 4.65, 4.0, 3.7, 3.8,
    "근본법 관념\n진보에 대한 믿음\n능률의 복음\n과학에 대한 신앙\n민주주의와 미국의 사명",
    fc="white", ec="#7a5fa8", fontsize=10.5)

box(ax, 8.8, 8.1, 3.7, 1.2, "운동과 모티프", fc="#f4fbf6", ec="#2f8f4e", fontsize=12, weight="bold")
box(ax, 8.8, 4.0, 3.7, 3.8,
    "행정조사운동(뷰로 운동)\n조직개편운동\n과학적 관리 운동\n행정훈련운동",
    fc="white", ec="#2f8f4e", fontsize=10.5)

for cx in (2.35, 6.5, 10.65):
    arrow(ax, cx, 3.9, cx if cx == 6.5 else (cx + (6.5 - cx) * 0.55), 2.6, color="#555")

box(ax, 2.9, 0.7, 7.2, 1.9,
    "행정학의 정통 교리\n= 시대의 산물이자 하나의 정치이론\n(『행정국가』가 해부한 대상)",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=11.5, weight="bold")

ax.text(6.5, 9.75, "왈도가 본 행정학의 토양 (『행정국가』 1부의 구도)",
        ha="center", fontsize=12.5, fontweight="bold")
fig.tight_layout()
fig.savefig(FIG / "fig11_background.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig11_*.png'))])
