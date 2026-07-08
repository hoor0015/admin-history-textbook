# 7주차 1차시 개념도 생성 (베버: 지배의 세 유형, 이념형 관료제)
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


# ---------------------------------------------------------------- 그림 7-1
# 지배의 세 유형
fig, ax = plt.subplots(figsize=(12, 6.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 3.1, 8.7, 5.8, 1.1, "지배: 명령이 복종을 얻어 내는 관계\n무엇이 복종을 정당하게 만드는가?",
    fc="#f7f7fc", ec="#5b6ee1", fontsize=11, weight="bold")

cols = [
    ("전통적 지배", "'옛날부터 늘 그래 왔다'\n\n근거: 관습과 세습\n예: 세습 군주, 가부장", "#fdf9f4", "#c77b2f"),
    ("카리스마적 지배", "'저 사람은 비범하다'\n\n근거: 개인의 비상한 자질\n예: 예언자, 전쟁 영웅", "#faf8fc", "#7a5fa8"),
    ("합법적 지배", "'절차에 따라 제정된\n규칙이다'\n\n근거: 법과 절차\n예: 근대 국가", "#f5f9fd", "#2f6fb0"),
]
for i, (t1, t2, fc, ec) in enumerate(cols):
    x = 0.5 + i * 4.0
    box(ax, x, 6.0, 3.2, 1.1, t1, fc=fc, ec=ec, fontsize=12, weight="bold")
    box(ax, x, 2.9, 3.2, 2.7, t2, fc="white", ec=ec, fontsize=10)
    arrow(ax, 6.0, 8.6, x + 1.6, 7.3, color="#888")

box(ax, 7.3, 0.6, 4.2, 1.5, "관료제\n합법적 지배가 일상 행정에서\n구현된 가장 순수한 형태",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=10, weight="bold")
arrow(ax, 10.1, 2.8, 9.6, 2.3, color="#2f6fb0", lw=2.0)
ax.text(2.2, 1.3, "복종의 근거가 '사람'에서 '규칙'으로 옮겨 갈수록\n근대적 지배에 가까워진다",
        ha="center", fontsize=10, color="#333",
        bbox=dict(fc="#f7f7fc", ec="#d9d9e3", boxstyle="round,pad=0.5"))
fig.savefig(FIG / "fig07_domination.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 7-2
# 이념형 관료제의 여섯 가지 특징
fig, ax = plt.subplots(figsize=(12, 6.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis("off")

box(ax, 4.3, 4.3, 3.4, 1.6, "근대 관료제\n(이념형)", fc="#f7f7fc", ec="#5b6ee1",
    fontsize=13, weight="bold")

feats_top = [
    ("관할권의 원칙", "법령이 정한\n권한과 의무"),
    ("계서제", "상급-하급의\n감독과 항소 체계"),
    ("문서주의", "기록에 기반한 사무\n공과 사의 분리"),
]
feats_bot = [
    ("전문훈련", "시험과 교육으로\n검증되는 자격"),
    ("전임직", "부업이 아닌 본업"),
    ("규칙에 따른 관리", "학습 가능한\n일반 규칙"),
]
for i, (t1, t2) in enumerate(feats_top):
    x = 0.5 + i * 4.0
    box(ax, x, 7.6, 3.2, 1.7, f"{t1}\n{t2}", fc="#f5f9fd", ec="#2f6fb0", fontsize=10)
    arrow(ax, x + 1.6, 7.5, 5.4 + (i - 1) * 0.9, 6.1, color="#888")
for i, (t1, t2) in enumerate(feats_bot):
    x = 0.5 + i * 4.0
    box(ax, x, 2.2, 3.2, 1.5, f"{t1}\n{t2}", fc="#f4fbf6", ec="#2f8f4e", fontsize=10)
    arrow(ax, x + 1.6, 3.8, 5.4 + (i - 1) * 0.9, 4.2, color="#888")

ax.text(6.0, 9.7, "조직의 구조", ha="center", fontsize=11, color="#2f6fb0", fontweight="bold")
ax.text(6.0, 1.5, "일하는 사람과 방식", ha="center", fontsize=11, color="#2f8f4e", fontweight="bold")
ax.text(6.0, 0.4, "공무원의 지위: 직업(소명)으로서의 직위 · 임명제 · 종신직 · 고정 급여와 연금 · 경력(승진)",
        ha="center", fontsize=10, color="#333",
        bbox=dict(fc="#fbf8f2", ec="#8a6d3b", boxstyle="round,pad=0.4"))
fig.savefig(FIG / "fig07_ideal_type.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig07_*.png'))])
