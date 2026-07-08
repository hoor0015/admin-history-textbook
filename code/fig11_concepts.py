# 11주차 개념도 생성 (그림 11-1, 11-2, 11-3, 11-4)
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
# 뿌리 방법 vs 가지 방법
fig, axes = plt.subplots(1, 2, figsize=(12, 6.4))
for ax in axes:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")

ax = axes[0]
ax.set_title("(가) 뿌리 방법: 합리적·총체적 접근", fontsize=13, pad=12)
steps_root = [
    "모든 관련 가치를 명료화하고\n중요도 순으로 서열화",
    "가능한 모든 정책대안 탐색",
    "각 대안의 모든 결과를\n포괄적으로 분석 (이론에 의존)",
    "목표를 최대로 달성하는\n최적 대안 선택",
]
y = 10.2
for i, t in enumerate(steps_root):
    box(ax, 1.6, y, 6.8, 1.6, t, fc="#f5f9fd", ec="#2f6fb0", fontsize=10.5)
    if i < 3:
        arrow(ax, 5.0, y - 0.15, 5.0, y - 0.85)
    y -= 2.5
ax.text(5.0, 1.2, "목표와 수단의 분리 · 처음부터 다시 계산\n요구되는 정보와 계산이 인간의 능력을 넘어선다",
        ha="center", fontsize=10, color="#333",
        bbox=dict(fc="#fdf9f4", ec="#c77b2f", boxstyle="round,pad=0.4"))

ax = axes[1]
ax.set_title("(나) 가지 방법: 연속적 제한 비교", fontsize=13, pad=12)
steps_branch = [
    "현재 정책(현상)에서 출발",
    "현재와 조금 다른\n소수의 익숙한 대안만 비교",
    "목표와 수단을 동시에 조정\n(경험이 이론을 대신한다)",
    "더 넓은 합의에 이른\n대안 선택 (작은 변화)",
]
y = 10.2
for i, t in enumerate(steps_branch):
    box(ax, 1.6, y, 6.8, 1.6, t, fc="#f4fbf6", ec="#2f8f4e", fontsize=10.5)
    if i < 3:
        arrow(ax, 5.0, y - 0.15, 5.0, y - 0.85)
    y -= 2.5
# 순환 화살표: 마지막 단계에서 첫 단계로
arrow(ax, 8.6, 3.5, 8.6, 10.6, color="#8a6d3b", ls="--")
ax.text(9.3, 7.0, "다시\n출발\n(연쇄)", ha="center", fontsize=9.5, color="#8a6d3b")
ax.text(5.0, 1.2, "선택된 작은 변화가 새 출발점이 된다\n비교의 연쇄가 곧 정책결정의 체계다",
        ha="center", fontsize=10, color="#333",
        bbox=dict(fc="#fbf8f2", ec="#8a6d3b", boxstyle="round,pad=0.4"))
fig.tight_layout()
fig.savefig(FIG / "fig11_root_branch.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 11-2
# 비교의 연쇄(위)와 상호조정(아래)
fig, axes = plt.subplots(2, 1, figsize=(11, 7.6))
for ax in axes:
    ax.axis("off")

ax = axes[0]
ax.set_xlim(0, 14)
ax.set_ylim(0, 6)
ax.set_title("(가) 비교의 연쇄: 작은 변화의 누적", fontsize=13, pad=10)
labels = ["현재 정책", "작은 수정 1", "작은 수정 2", "작은 수정 3"]
for i, t in enumerate(labels):
    x = 0.5 + i * 3.0
    box(ax, x, 3.6, 2.4, 1.4, t, fc="#f4fbf6", ec="#2f8f4e", fontsize=10.5)
    if i < 3:
        arrow(ax, x + 2.5, 4.3, x + 2.9, 4.3, color="#2f8f4e")
box(ax, 12.6, 3.6, 1.1, 1.4, "…", fc="white", ec="#2f8f4e", fontsize=13)
ax.text(6.5, 5.6, "각 단계는 앞 단계에서 축적된 지식을 활용한다", ha="center",
        fontsize=10, color="#555")
arrow(ax, 1.7, 3.4, 12.0, 1.5, color="#c0392b", ls="--")
box(ax, 10.9, 0.4, 2.9, 1.3, "한 번의 큰 도약", fc="#fdf3f2", ec="#c0392b", fontsize=10.5)
ax.text(5.6, 1.6, "돌이킬 수 없는 큰 실수의 위험", fontsize=10, color="#c0392b",
        rotation=-8, ha="center")

ax = axes[1]
ax.set_xlim(0, 14)
ax.set_ylim(0, 6.6)
ax.set_title("(나) 상호조정: 분업된 종합성", fontsize=13, pad=10)
agencies = [("교육 기관", 1.0), ("보건 기관", 5.7), ("경찰 기관", 10.4)]
for t, x in agencies:
    box(ax, x, 4.2, 2.6, 1.4, t + "\n(자기 영역의 가치에 집중)", fc="#f5f9fd",
        ec="#2f6fb0", fontsize=9.8)
arrow(ax, 3.7, 4.9, 5.6, 4.9, color="#8a6d3b")
arrow(ax, 5.6, 4.6, 3.7, 4.6, color="#8a6d3b")
arrow(ax, 8.4, 4.9, 10.3, 4.9, color="#8a6d3b")
arrow(ax, 10.3, 4.6, 8.4, 4.6, color="#8a6d3b")
ax.text(4.65, 5.3, "견제·협상", ha="center", fontsize=9, color="#8a6d3b")
ax.text(9.35, 5.3, "견제·협상", ha="center", fontsize=9, color="#8a6d3b")
box(ax, 4.2, 0.7, 5.6, 1.7, "전체 정부 수준의 종합성\n(어느 한 기관의 편향도\n다른 기관이 보정한다)",
    fc="#fbf8f2", ec="#8a6d3b", fontsize=10)
for _, x in agencies:
    arrow(ax, x + 1.3, 4.0, 7.0, 2.6, color="#999")
fig.tight_layout()
fig.savefig(FIG / "fig11_chain.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 11-3
# 행정 가치의 세 기둥
fig, ax = plt.subplots(figsize=(10, 5.6))
ax.set_xlim(0, 12)
ax.set_ylim(0, 9)
ax.axis("off")
# 지붕
box(ax, 1.2, 6.6, 9.6, 1.5, "행정 (public administration)", fc="#f7f7fc",
    ec="#5b6ee1", fontsize=13, weight="bold")
# 세 기둥
pillars = [
    ("능률성\n(efficiency)", "고전 행정학의 가치\n(윌슨 이후)", "#f5f9fd", "#2f6fb0"),
    ("경제성\n(economy)", "고전 행정학의 가치\n(윌슨 이후)", "#f5f9fd", "#2f6fb0"),
    ("사회적 형평성\n(social equity)", "신행정학이 추가\n(미노브룩, 1968)", "#fbf8f2", "#8a6d3b"),
]
for i, (t1, t2, fc, ec) in enumerate(pillars):
    x = 1.6 + i * 3.2
    box(ax, x, 3.0, 2.6, 3.2, t1, fc=fc, ec=ec, fontsize=11.5, weight="bold")
    box(ax, x, 1.1, 2.6, 1.5, t2, fc="white", ec=ec, fontsize=9.5)
ax.text(6.0, 0.3, "세 번째 기둥이 던지는 질문: 이 서비스는 누구를 위한 것인가",
        ha="center", fontsize=11, color="#333")
fig.savefig(FIG / "fig11_pillars.png", dpi=150, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- 그림 11-4
# 격동의 1960년대와 미노브룩 회의 연표
fig, ax = plt.subplots(figsize=(11.5, 4.6))
ax.set_xlim(1962.5, 1972.5)
ax.set_ylim(-3.2, 3.4)
ax.axis("off")
ax.axhline(0, color="#555", lw=1.6)
events = [
    (1964, 1, "1964\n시민권법 제정"),
    (1965, -1, "1965\n와츠(로스앤젤레스) 폭동\n'위대한 사회' 입법"),
    (1967, 1, "1967\n디트로이트 등\n도시 폭동 확산"),
    (1968, -1, "1968\n킹 목사·로버트 케네디 암살\n베트남전 반대 시위 격화"),
    (1968.55, 1.15, "1968년 9월\n미노브룩 회의\n(시라큐스대, 왈도 주선)"),
    (1971, -1, "1971\n『신행정학을 향하여』 출간\n(마리니 편)"),
]
for yr, side, label in events:
    color = "#8a6d3b" if "미노브룩" in label else "#2f6fb0"
    ax.plot([yr], [0], "o", color=color, ms=8, zorder=3)
    ax.plot([yr, yr], [0, side * 0.55], color=color, lw=1.2)
    va = "bottom" if side > 0 else "top"
    ax.text(yr, side * 0.7, label, ha="center", va=va, fontsize=9.6,
            color="#333",
            bbox=dict(fc="#fbf8f2" if "미노브룩" in label else "white",
                      ec=color, boxstyle="round,pad=0.35", lw=1.1))
for yr in range(1963, 1973):
    ax.plot([yr], [0], "|", color="#999", ms=10)
    ax.text(yr, -0.35, str(yr), ha="center", va="top", fontsize=8.5, color="#777")
ax.set_title("격동의 1960년대: 미노브룩 회의로 가는 길", fontsize=13, pad=12)
fig.savefig(FIG / "fig11_sixties.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("saved:", [p.name for p in sorted(FIG.glob('fig11_*.png'))])
