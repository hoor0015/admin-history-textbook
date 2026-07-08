# 8주차 1차시 개념도 생성 (해링: 관료제와 공익)
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


# ---------------------------------------------------------------- 그림 8-1
# 행정국가 팽창 연표 (1929-1945)
fig, ax = plt.subplots(figsize=(12.5, 5.6))
ax.set_xlim(1927.0, 1947.5)
ax.set_ylim(0, 10)
ax.axis("off")

# 기준선
arrow(ax, 1927.5, 5.0, 1947.0, 5.0, color="#333", lw=2.0)
for yr in (1930, 1935, 1940, 1945):
    ax.plot([yr, yr], [4.85, 5.15], color="#333", lw=1.2)
    ax.text(yr, 4.35, str(yr), ha="center", fontsize=10, color="#333")

# (연도, 라벨, 위치 y, 색상 fc, ec)
events = [
    (1929, "주가 대폭락\n대공황 시작", 8.2, "#fdf9f4", "#c77b2f"),
    (1933, "루스벨트 취임\n백일의회\n(AAA·CCC·TVA 등)", 0.9, "#f4fbf6", "#2f8f4e"),
    (1935, "제2차 뉴딜\n사회보장법·WPA", 6.6, "#f4fbf6", "#2f8f4e"),
    (1936, "해링\n『행정과 공익』", 2.5, "#f5f9fd", "#2f6fb0"),
    (1938, "브라운로 위원회 보고서(1937)\n귤릭 「조직이론에 관한 노트」", 8.4, "#f5f9fd", "#2f6fb0"),
    (1940, "재조직법(1939)\n대통령실(EOP) 신설", 0.9, "#faf8fc", "#7a5fa8"),
    (1942, "미국 참전(1941)\n전시 동원 체제", 6.6, "#fdf9f4", "#c77b2f"),
    (1945, "종전\n행정국가의 정착", 2.5, "#faf8fc", "#7a5fa8"),
]
BW, BH = 3.6, 1.5
for yr, label, ypos, fc, ec in events:
    # 표시 지점(굵은 점)은 실제 연도, 상자는 겹침 방지를 위해 약간 이동 가능
    dot_year = {1938: 1937, 1940: 1939, 1942: 1941}.get(yr, yr)
    ax.plot(dot_year, 5.0, "o", color=ec, ms=7, zorder=5)
    x0 = yr - BW / 2
    x0 = min(max(x0, 1927.3), 1947.2 - BW)
    box(ax, x0, ypos, BW, BH, label, fc=fc, ec=ec, fontsize=9.5)
    if ypos > 5:
        ax.plot([dot_year, yr], [5.2, ypos - 0.12], color=ec, lw=1.1, ls=":")
    else:
        ax.plot([dot_year, yr], [4.8, ypos + BH + 0.12], color=ec, lw=1.1, ls=":")

ax.set_title("행정국가의 팽창 (1929-1945): 위기, 뉴딜, 그리고 제도화", fontsize=13, pad=10)
fig.savefig(FIG / "fig08_timeline.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 8-2
# 정치적 합의의 번역자: 관료를 둘러싼 이해관계의 거미줄
fig, ax = plt.subplots(figsize=(11, 5.8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

box(ax, 0.4, 3.2, 3.0, 1.9, "의회\n일반 원칙만 담은 법률\n(정치적 타협)", fc="#fdf9f4", ec="#c77b2f")
box(ax, 4.4, 3.2, 3.2, 1.9, "관료(행정가)\n재량의 여지 안에서\n공익을 해석", fc="#f5f9fd", ec="#2f6fb0", weight="bold")
box(ax, 8.6, 3.2, 3.0, 1.9, "구체적 상황에 적용\n(집행: 규칙·기준·판정)", fc="#faf8fc", ec="#7a5fa8")
box(ax, 4.4, 6.2, 3.2, 1.4, "법원\n권한의 범위를 한정", fc="#f4fbf6", ec="#2f8f4e", fontsize=10)
box(ax, 4.4, 0.4, 3.2, 1.4, "이익집단·시민\n요구, 비판, '정치적 연줄'", fc="#fdf9f4", ec="#c77b2f", fontsize=10)

arrow(ax, 3.5, 4.15, 4.3, 4.15)
ax.text(3.9, 4.5, "위임", ha="center", fontsize=9.5, color="#555")
arrow(ax, 7.7, 4.15, 8.5, 4.15)
ax.text(8.1, 4.5, "번역", ha="center", fontsize=9.5, color="#555")
arrow(ax, 6.0, 6.1, 6.0, 5.3, color="#2f8f4e")
arrow(ax, 5.6, 1.9, 5.6, 3.1, color="#c77b2f")
arrow(ax, 6.4, 3.1, 6.4, 1.9, color="#c77b2f")
ax.text(7.0, 2.4, "압력과 반응", fontsize=9.5, color="#555")

ax.text(1.9, 1.2, "법은 진공 속에서\n집행되지 않는다.", ha="center", fontsize=10.5, color="#333",
        bbox=dict(fc="#fbf8f2", ec="#8a6d3b", boxstyle="round,pad=0.5"))
ax.set_title("정치적 합의의 번역자: 관료를 둘러싼 이해관계의 거미줄", fontsize=13, pad=10)
fig.savefig(FIG / "fig08_web.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig08_*.png'))])
