# 9주차 1차시 그림: 머튼의 관료제 역기능 인과 구조
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


# ---------------------------------------------------------------- 그림 9-1
# 머튼의 역기능 인과 구조도 (신뢰성 요구 -> 규율 -> 목표 대치 -> 비효율)
fig, ax = plt.subplots(figsize=(11, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 13)
ax.axis("off")

cx, cw = 4.6, 4.8  # 중앙 사슬 x, 폭

# 중앙 인과 사슬 (위에서 아래로)
box(ax, cx, 11.0, cw, 1.5, "기능적 요구\n반응의 신뢰성, 규정된 행위 양식에 대한 순응",
    fc="#fdf9f4", ec="#c77b2f", fontsize=10.5, weight="bold")
box(ax, cx, 8.7, cw, 1.5, "규율과 정서의 과잉 주입\n필요 이상으로 고양된 의무감 (안전 여유)",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5)
box(ax, cx, 6.4, cw, 1.5, "목표 대치\n정서가 목표에서 규칙의 세부로 전이,\n규칙의 절대화 (수단이 목적이 됨)",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=10)
box(ax, cx, 4.1, cw, 1.5, "경직성과 형식주의\n의례주의, 레드테이프, '관료적 거장'",
    fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5)
box(ax, cx, 1.5, cw, 1.7, "특수 상황에서의 부적응\n일반적으로 효율을 높이는 요소들이\n구체적 사례에서 비효율을 낳는다",
    fc="#faf8fc", ec="#7a5fa8", fontsize=10.5, weight="bold")

for y1, y2 in [(11.0, 10.3), (8.7, 8.0), (6.4, 5.7), (4.1, 3.3)]:
    arrow(ax, cx + cw / 2, y1, cx + cw / 2, y2)

# 왼쪽 강화 장치
box(ax, 0.3, 9.0, 3.4, 1.5, "경력 장치\n연금, 근속 승진,\n승급형 급여", fc="#f4fbf6", ec="#2f8f4e", fontsize=10)
box(ax, 0.3, 6.2, 3.4, 1.5, "전우애와\n비공식 조직\n(낮은 내부 경쟁)", fc="#f4fbf6", ec="#2f8f4e", fontsize=10)
arrow(ax, 3.8, 9.6, cx - 0.1, 9.5, color="#2f8f4e")
arrow(ax, 3.8, 7.0, cx - 0.1, 7.1, color="#2f8f4e")

# 오른쪽 강화 장치
box(ax, 10.3, 9.0, 3.4, 1.5, "규범의 성화\n기술적 규칙이\n상징이 되고 굳어짐", fc="#f4fbf6", ec="#2f8f4e", fontsize=10)
box(ax, 10.3, 6.2, 3.4, 1.5, "비인격성과 범주화\n개별 사례의\n특수성 무시", fc="#f4fbf6", ec="#2f8f4e", fontsize=10)
arrow(ax, 10.2, 9.6, cx + cw + 0.1, 9.5, color="#2f8f4e")
arrow(ax, 10.2, 7.0, cx + cw + 0.1, 7.1, color="#2f8f4e")

# 범례성 주석
ax.text(2.0, 4.6, "초록 상자:\n사슬을 강화하는\n구조적 장치", ha="center", fontsize=9.5, color="#2f8f4e")
ax.text(12.0, 4.6, "주황: 출발점(성공 조건)\n파랑: 변형 과정\n보라: 역설적 결과", ha="center", fontsize=9.5, color="#555")
ax.set_title("머튼의 관료제 역기능 인과 구조: 신뢰성 요구에서 비효율까지", fontsize=13, pad=14)

fig.tight_layout()
fig.savefig(FIG / "fig09_merton_dysfunction.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("saved:", FIG / "fig09_merton_dysfunction.png")
