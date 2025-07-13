const express = require('express');
const cors = require('cors');
const app = express();
const port = process.env.PORT || 3000;

app.use(cors());

const completedTasks = {};

app.get('/postback', (req, res) => {
  const { aff_sub, payout, ip, type } = req.query;
  if (!aff_sub || !type) return res.status(400).send('Missing aff_sub or type');

  if (!completedTasks[aff_sub]) completedTasks[aff_sub] = {};
  completedTasks[aff_sub][type] = true;

  console.log(`✅ Postback: ${aff_sub} | ${type} | $${payout} | IP: ${ip}`);
  res.send('OK');
});

app.get('/check_task', (req, res) => {
  const { aff_sub, type } = req.query;
  if (!aff_sub || !type) return res.status(400).json({ error: 'Missing aff_sub or type' });

  const completed = completedTasks[aff_sub]?.[type] === true;
  if (completed) completedTasks[aff_sub][type] = false;

  res.json({ completed });
});

app.listen(port, () => {
  console.log(`🚀 Server running on port ${port}`);
});
