# 4주차 1차시 그림 4-1: 엽관제에서 실적주의로, 그리고 행정학의 탄생으로 (1801-1887)
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


def arrow(ax, x1, y1, x2, y2, color="#555", style="-|>", lw=1.4, ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=14, color=color, lw=lw, linestyle=ls))


fig, ax = plt.subplots(figsize=(13, 5.8))
ax.set_xlim(1790, 1906)
ax.set_ylim(0, 10)
ax.axis("off")

# 중앙 시간축
AXIS_Y = 5.6
arrow(ax, 1792, AXIS_Y, 1904, AXIS_Y, color="#333", lw=2.0)
for yr in [1801, 1829, 1832, 1871, 1880, 1881, 1883, 1887]:
    ax.plot([yr, yr], [AXIS_Y - 0.13, AXIS_Y + 0.13], color="#333", lw=1.6)
ax.text(1801, AXIS_Y + 0.35, "1801", ha="center", fontsize=10, color="#333")
ax.text(1829, AXIS_Y + 0.35, "1829", ha="center", fontsize=10, color="#333")
ax.text(1832, AXIS_Y - 0.75, "1832", ha="center", fontsize=10, color="#333")
ax.text(1871, AXIS_Y + 0.35, "1871", ha="center", fontsize=10, color="#333")
ax.text(1881, AXIS_Y + 0.35, "1881", ha="center", fontsize=10, color="#333")
ax.text(1887, AXIS_Y + 0.35, "1887", ha="center", fontsize=10, color="#333")
# 1880·1883은 눈금만 표시 (연도는 상자 안에 있음, 라벨 겹침 방지)

# 시대 라벨
ax.text(1818, 2.0, "엽관제의 시대", ha="center", fontsize=13, fontweight="bold", color="#c77b2f")
ax.text(1856, 8.2, "개혁의 시대와 행정학의 탄생", ha="center", fontsize=13,
        fontweight="bold", color="#2f8f4e")

# 위쪽 줄: 엽관제의 시대 (주황)
box(ax, 1794, 7.1, 14, 2.1, "1801 제퍼슨의 원칙\n\"정치적 의견 차이는\n해임 사유가 아니다\"",
    fc="#fdf9f4", ec="#c77b2f", fontsize=9.5)
arrow(ax, 1801, 7.0, 1801, AXIS_Y + 0.2, color="#c77b2f")
box(ax, 1816, 3.3, 13, 2.1, "1829 잭슨 취임\n공직 순환 교리\n(반귀족주의)",
    fc="#fdf9f4", ec="#c77b2f", fontsize=9.5)
arrow(ax, 1829, AXIS_Y - 0.2, 1825, 5.5, color="#c77b2f")
box(ax, 1826, 7.1, 15, 2.1, "1832 마시의 상원 연설\n\"전리품은 승자의 것\"\n엽관제라는 이름의 기원",
    fc="#fdf9f4", ec="#c77b2f", fontsize=9.5)
arrow(ax, 1832, AXIS_Y + 0.2, 1834, 7.0, color="#c77b2f")

# 아래쪽 줄: 개혁의 시대 (초록) + 행정학 탄생 (보라), 두 단으로 엇갈리게 배치
box(ax, 1854.5, 3.3, 12, 2.1, "1871 그랜트, 최초의\n공무원위원회 설치\n(1875년 좌초)",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=9.5)
arrow(ax, 1871, AXIS_Y - 0.2, 1865, 5.5, color="#2f8f4e")
box(ax, 1868, 0.6, 12, 2.1, "1880 이튼\n『영국의 공무원제도』\n실적제 도입 주장",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=9.5)
arrow(ax, 1880, AXIS_Y - 0.2, 1876, 2.8, color="#2f8f4e")
box(ax, 1869, 6.4, 12, 2.1, "1881 가필드 암살\n(7월 피격, 9월 사망)\n개혁 여론 결집",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=9.5)
arrow(ax, 1881, AXIS_Y + 0.2, 1877, 6.3, color="#2f8f4e")
box(ax, 1882.5, 3.3, 13.5, 2.1, "1883 펜들턴법\n공개 경쟁시험·실적 승진\n·공무원위원회",
    fc="#f4fbf6", ec="#2f8f4e", fontsize=9.5)
arrow(ax, 1883, AXIS_Y - 0.2, 1886, 5.5, color="#2f8f4e")
box(ax, 1885, 6.4, 14, 2.1, "1887 윌슨 「행정학 연구」\n행정학의 탄생\n(펜들턴법 4년 뒤)",
    fc="#faf8fc", ec="#7a5fa8", fontsize=9.5, weight="bold")
arrow(ax, 1887, AXIS_Y + 0.2, 1890, 6.3, color="#7a5fa8")

fig.tight_layout()
fig.savefig(FIG / "fig04_timeline.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("saved:", FIG / "fig04_timeline.png")
