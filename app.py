def home():
    return "خادم نظام زيادة المتابعين يعمل بكفاءة على السحابة!"

@app.route('/add-followers', methods=['POST'])
def add_followers():
    data = request.json
    if not data:
        return jsonify({"error": "الرجاء إرسال البيانات بصيغة JSON"}), 400
        
    username = data.get('username')
    count = data.get('count')
    
    if not username or not count:
        return jsonify({"error": "الرجاء إدخال اسم المستخدم والعدد المطلوب"}), 400
    
    # إضافة الطلب إلى القائمة
    task = {"username": username, "count": count, "status": "pending"}
    tasks_queue.append(task)
    
    print(f"تم استلام طلب سحابي لزيادة {count} متابع للحساب: {username}")
    
    return jsonify({
        "status": "success",
        "message": "تم إضافة الطلب إلى طابور الانتظار بنجاح",
        "task_details": task
    }), 200

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"total_tasks": len(tasks_queue), "tasks": tasks_queue}), 200

if __name__ == '__main__':
    # السحابة تتطلب قراءة رقم المنفذ (Port) تلقائياً من النظام
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
