
from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash
)

app = Flask(__name__)
app.secret_key = "dev-secret-key"

USERS = {"test-user" :{"password" : "1234"}}

PRODUCTS = [
    {
        "id": 1,
        "name": "Air Runner 1",
        "price": 89000,
        "brand": "Resona Sport",
        "description": "가볍고 통풍이 잘 되는 러닝화. 일상 & 운동 모두에 적합한 베이직 러너.",
        "image_url": "https://images.pexels.com/photos/2529159/pexels-photo-2529159.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 2,
        "name": "Street Walker",
        "price": 99000,
        "brand": "Urban Line",
        "description": "도심 라이프스타일에 맞춘 심플 스니커즈. 데님과 찰떡궁합.",
        "image_url": "https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 3,
        "name": "Classic Leather",
        "price": 129000,
        "brand": "Premium Co.",
        "description": "포멀룩에 어울리는 천연 가죽 드레스 슈즈.",
        "image_url": "https://images.pexels.com/photos/7691262/pexels-photo-7691262.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 4,
        "name": "Trail Hiker",
        "price": 139000,
        "brand": "Mountain Gear",
        "description": "방수 기능과 견고한 밑창으로 산행에 최적화된 하이킹 부츠.",
        "image_url": "https://images.pexels.com/photos/7625049/pexels-photo-7625049.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 5,
        "name": "Court Master",
        "price": 119000,
        "brand": "Resona Sport",
        "description": "테니스 및 코트 스포츠를 위한 안정적인 쿠션감.",
        "image_url": "https://images.pexels.com/photos/1124465/pexels-photo-1124465.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 6,
        "name": "City Loafer",
        "price": 99000,
        "brand": "Urban Line",
        "description": "슬랙스/청바지 모두 잘 어울리는 데일리 로퍼.",
        "image_url": "https://images.pexels.com/photos/7691241/pexels-photo-7691241.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 7,
        "name": "Canvas Breeze",
        "price": 69000,
        "brand": "SimpleWear",
        "description": "가벼운 캔버스 소재로 여름철에 안성맞춤.",
        "image_url": "https://images.pexels.com/photos/2529146/pexels-photo-2529146.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 8,
        "name": "Winter Boot",
        "price": 149000,
        "brand": "ColdProof",
        "description": "보온과 방수를 모두 잡은 겨울 부츠.",
        "image_url": "https://images.pexels.com/photos/7691251/pexels-photo-7691251.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 9,
        "name": "Minimal Slide",
        "price": 39000,
        "brand": "SimpleWear",
        "description": "집 안/밖 모두 활용 가능한 미니멀 슬라이드 샌들.",
        "image_url": "https://images.pexels.com/photos/19090/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=600"
    },
    {
        "id": 10,
        "name": "Kids Runner",
        "price": 59000,
        "brand": "Resona Kids",
        "description": "아이들을 위한 경량 러닝화, 부드러운 쿠션과 안전한 접지력.",
        "image_url": "https://images.pexels.com/photos/1078640/pexels-photo-1078640.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
]

def get_product(pid):
    return next((p for p in PRODUCTS if p["id"] == pid), None)

@app.context_processor
def inject_globals():
    cart = session.get("cart", {})
    return {
        "current_user": session.get("user_id"),
        "cart_count": len(cart),
        "product_in_cart": lambda pid: str(pid) in cart,
    }

def require_login():
    if not session.get("user_id"):
        flash("로그인이 필요합니다.", "warning")
        return False
    return True

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)

@app.route("/product/<int:pid>")
def product_detail(pid):
    product = get_product(pid)
    if not product:
        flash("상품이 존재하지 않습니다.", "danger")
        return redirect(url_for("index"))
    return render_template("product_detail.html", product=product)

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    items = []
    total = 0
    for pid_str in cart:
        product = get_product(int(pid_str))
        if product:
            total += product["price"]
            items.append(product)
    return render_template("cart.html", items=items, total=total)

@app.route("/cart/toggle/<int:pid>", methods=["POST"])
def toggle_cart(pid):
    if not require_login():
        return redirect(url_for("login", next=request.referrer or url_for("index")))
    cart = session.get("cart", {})
    pid_str = str(pid)
    if pid_str in cart:
        cart.pop(pid_str)
        flash("장바구니에서 제거되었습니다.", "info")
    else:
        cart[pid_str] = 1
        flash("장바구니에 추가되었습니다.", "success")
    session["cart"] = cart
    return redirect(request.referrer or url_for("index"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if not require_login():
        return redirect(url_for("login", next=url_for("checkout")))
    if not session.get("cart"):
        flash("장바구니가 비어 있습니다.", "warning")
        return redirect(url_for("index"))
    if request.method == "POST":
        if "cancel" in request.form:
            flash("결제가 취소되었습니다.", "info")
            return redirect(url_for("cart"))
        name = request.form.get("name","").strip()
        phone = request.form.get("phone","").strip()
        address = request.form.get("address","").strip()
        if not (name and phone and address):
            flash("모든 필수 정보를 입력해주세요.", "danger")
        else:
            session["cart"] = {}
            flash("결제가 완료되었습니다! 주문이 접수되었습니다.", "success")
            return redirect(url_for("index"))
    return render_template("checkout.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["username"].strip()
        password=request.form["password"].strip()
        user=USERS.get(username)
        if not user or user["password"]!=password:
            flash("아이디 또는 비밀번호가 올바르지 않습니다.","danger")
        else:
            session["user_id"]=username
            flash("로그인 성공!","success")
            next_url = request.args.get("next")
            return redirect(next_url or url_for("index"))
    return render_template("login.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form["username"].strip()
        password=request.form["password"].strip()
        confirm=request.form["confirm"].strip()
        if username in USERS:
            flash("이미 존재하는 사용자입니다.","danger")
        elif password!=confirm:
            flash("비밀번호가 일치하지 않습니다.","danger")
        else:
            USERS[username]={"password":password}
            flash("회원가입 성공! 이제 로그인해주세요.","success")
            return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("로그아웃되었습니다.","info")
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(debug=True)
