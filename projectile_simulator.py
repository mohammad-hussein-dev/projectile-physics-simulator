import math
import matplotlib.pyplot as plt

# دریافت ورودی از کاربر
v0 = float(input("سرعت اولیه (m/s) را وارد کنید: "))
theta_deg = float(input("زاویه (درجه) را وارد کنید: "))

# تبدیل زاویه به رادیان
theta = math.radians(theta_deg)

# ثابت گرانش (m/s²)
g = 9.8

# محاسبات فیزیک
R = (v0 ** 2 * math.sin(2 * theta)) / g
H = (v0 ** 2 * (math.sin(theta) ** 2)) / (2 * g)
T = 2 * v0 * math.sin(theta) / g

# چاپ نتایج
print(f"\n📊 نتایج:")
print(f"برد پرتابه: {R:.2f} متر")
print(f"حداکثر ارتفاع: {H:.2f} متر")
print(f"زمان کل پرواز: {T:.2f} ثانیه")

# تولید نقاط مسیر
t = [i / 100 for i in range(int(T * 100) + 1)]
x = [v0 * math.cos(theta) * ti for ti in t]
y = [v0 * math.sin(theta) * ti - 0.5 * g * ti ** 2 for ti in t]

# رسم نمودار
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='blue', linewidth=2)
plt.title('مسیر حرکت پرتابه')
plt.xlabel('فاصله افقی (متر)')
plt.ylabel('ارتفاع (متر)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)
plt.xlim(0, max(x) + 1)
plt.ylim(0, max(y) + 1)
plt.show()
