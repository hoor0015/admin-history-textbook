# 13주차 개념도 생성 (그림 13-1, 12-2)
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


# ---------------------------------------------------------------- 그림 13-1
# 예산개혁의 3단계 연표 (쉬크, 1966)
fig, ax = plt.subplots(figsize=(12, 5.6))
ax.set_xlim(1912, 1978)
ax.set_ylim(0, 10)
ax.axis("off")

# 단계 상자 (위)
stages = [
    (1920, 1935, "1단계 통제 지향\n품목별 예산\n(지출의 합법성)", "#fdf9f4", "#c77b2f"),
    (1935, 1960, "2단계 관리 지향\n성과주의 예산\n(작업의 능률)", "#f4fbf6", "#2f8f4e"),
    (1960, 1975, "3단계 기획 지향\nPPBS(프로그램 예산)\n(목표와 대안의 선택)", "#f5f9fd", "#2f6fb0"),
]
for x0, x1, label, fc, ec in stages:
    box(ax, x0 + 0.4, 5.6, x1 - x0 - 0.8, 3.2, label, fc=fc, ec=ec, fontsize=11.5, weight="bold")
arrow(ax, 1934.7, 7.2, 1936.1, 7.2, color="#777")
arrow(ax, 1959.7, 7.2, 1961.1, 7.2, color="#777")

# 시간축
ax.plot([1915, 1976], [4.6, 4.6], color="#555", lw=1.6)
for yr in range(1915, 1980, 5):
    ax.plot([yr, yr], [4.45, 4.75], color="#555", lw=1.1)
    ax.text(yr, 4.0, str(yr), ha="center", fontsize=9.5, color="#555")

# 주요 사건 (아래)
events = [
    (1921, "1921 예산회계법\n(연방 예산제도 출발)", "#c77b2f"),
    (1937, "1937 브라운로 위원회\n(관리 기구로의 전환 촉구)", "#2f8f4e"),
    (1949, "1949 후버 위원회\n(성과주의 예산 권고)", "#2f8f4e"),
    (1961, "1961 국방부\nPPBS 도입(맥나마라)", "#2f6fb0"),
    (1965, "1965 존슨,\n전 부처 확대", "#2f6fb0"),
    (1971, "1971 연방 PPB\n사실상 폐기", "#8a6d3b"),
]
levels = [2.6, 1.0, 2.6, 1.0, 2.6, 1.0]
for (yr, label, color), lv in zip(events, levels):
    ax.plot([yr, yr], [4.6, lv + 0.55], color=color, lw=1.0, ls=":")
    ax.text(yr, lv, label, ha="center", va="top", fontsize=9.5, color=color)

ax.text(1944, 9.6, "예산개혁의 3단계: 강조점의 이동 (앞 단계의 기능은 사라지지 않고 그 위에 쌓인다)",
        ha="center", fontsize=12.5, fontweight="bold")
fig.savefig(FIG / "fig13_budget_stages.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 13-2
# 시스템 분석 대 정책분석 (드로어, 1967)
fig, ax = plt.subplots(figsize=(12, 6.4))
ax.set_xlim(0, 12)
ax.set_ylim(0, 11)
ax.axis("off")

box(ax, 0.6, 9.1, 4.6, 1.3, "시스템 분석\n(경제학·계량적 의사결정 이론)", fc="#fdf9f4", ec="#c77b2f",
    fontsize=11.5, weight="bold")
box(ax, 6.8, 9.1, 4.6, 1.3, "정책분석\n(+ 개편된 정치학·행정학)", fc="#f5f9fd", ec="#2f6fb0",
    fontsize=11.5, weight="bold")

sa = [
    "모든 결정을 자원 배분 문제로 환원",
    "계량 모델과 수치에 의존",
    "정치적 실현 가능성을 무시",
    "주어진 대안들의 비교",
    "명확한 기준과 최적해 추구",
]
pa = [
    "자원 배분을 넘어선 넓은 의사결정 개념",
    "질적 방법·암묵지·훈련된 직관을 통합",
    "정치와 가치를 분석의 중심에",
    "새로운 대안의 창안 (창의성·혁신)",
    "순차적 결정과 지속적 학습, 미래 지향",
]
for i, (l, r) in enumerate(zip(sa, pa)):
    y = 7.5 - i * 1.35
    box(ax, 0.6, y, 4.6, 1.05, l, fc="white", ec="#c77b2f", fontsize=10)
    box(ax, 6.8, y, 4.6, 1.05, r, fc="white", ec="#2f6fb0", fontsize=10)
    arrow(ax, 5.35, y + 0.52, 6.65, y + 0.52, color="#7a5fa8")

ax.text(6.0, 10.35, "혼합(mix)이 아닌 화합물(compound)로", ha="center", va="center",
        fontsize=10.5, color="#7a5fa8", fontweight="bold")
arrow(ax, 5.35, 9.75, 6.65, 9.75, color="#7a5fa8", lw=2.2)

box(ax, 3.1, 0.3, 5.8, 1.2, "정책과학(policy sciences)의 기초\n\"과학과 정치 사이의 다리\"",
    fc="#faf8fc", ec="#7a5fa8", fontsize=10.5)
arrow(ax, 9.1, 2.05, 7.6, 1.6, color="#7a5fa8")
fig.savefig(FIG / "fig13_sa_vs_pa.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig13_*.png'))])
