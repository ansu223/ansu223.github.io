// server.js (Node.js Backend)
const express = require('express');
const app = express();
const cors = require('cors');
app.use(cors());
app.use(express.json());

let users = {}; // Store user balances and referrals

// Spin Game API
app.post('/api/spin', (req, res) => {
    const userId = req.body.userId;
    if (!users[userId]) users[userId] = { balance: 0, referredBy: null };
    
    const rewards = [10, 20, 50, 100, 200];
    const reward = rewards[Math.floor(Math.random() * rewards.length)];
    users[userId].balance += reward;
    res.json({ success: true, reward, balance: users[userId].balance });
});

// Referral System API
app.post('/api/referral', (req, res) => {
    const { userId, referrerId } = req.body;
    if (!users[userId]) users[userId] = { balance: 0, referredBy: referrerId };
    if (users[referrerId]) users[referrerId].balance += 50; // Reward referrer
    res.json({ success: true, balance: users[referrerId]?.balance || 0 });
});

// Wallet System API
app.get('/api/balance', (req, res) => {
    const userId = req.query.userId;
    res.json({ balance: users[userId]?.balance || 0 });
});

app.post('/api/withdraw', (req, res) => {
    const userId = req.body.userId;
    const amount = req.body.amount;
    if (users[userId] && users[userId].balance >= amount) {
        users[userId].balance -= amount;
        res.json({ success: true, balance: users[userId].balance });
    } else {
        res.status(400).json({ success: false, message: 'Insufficient balance' });
    }
});

app.listen(3000, () => console.log('Server running on port 3000'));

// frontend.html (Client-side UI)
/*
<!DOCTYPE html>
<html>
<head>
    <title>Giftbox Spin Game</title>
</head>
<body>
    <h1>Spin to Win!</h1>
    <button onclick="spinWheel()">Spin</button>
    <p id="result"></p>
    <h2>Your Balance: <span id="balance">0</span> BTTC</h2>
    <button onclick="withdraw()">Withdraw 50 BTTC</button>

    <script>
        let userId = 'user123';

        function spinWheel() {
            fetch('/api/spin', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ userId }) })
            .then(res => res.json())
            .then(data => {
                document.getElementById('result').innerText = 'You won ' + data.reward + ' BTTC!';
                document.getElementById('balance').innerText = data.balance;
            });
        }

        function withdraw() {
            fetch('/api/withdraw', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ userId, amount: 50 }) })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    alert('Withdrawal successful!');
                    document.getElementById('balance').innerText = data.balance;
                } else {
                    alert(data.message);
                }
            });
        }
    </script>
</body>
</html>
*/
