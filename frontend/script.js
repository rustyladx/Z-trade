const statusEl = document.getElementById("status");
const resultEl = document.getElementById("result");

async function fetchSignal() {
  statusEl.innerText = "Analyzing market...";

  try {
    const res = await fetch("https://your-api-url.com/api/signal");
    const data = await res.json();

    statusEl.innerText = "Trade Suggestion:";
    resultEl.innerHTML = `
      <strong>Coin:</strong> ${data.coin}<br>
      <strong>Strategy:</strong> ${data.strategy}<br>
      <strong>Entry:</strong> ${data.entry}<br>
      <strong>Exit:</strong> ${data.exit}<br>
      <strong>Take Profit:</strong> ${data.tp}<br>
      <strong>Stop Loss:</strong> ${data.sl}
    `;
  } catch (err) {
    statusEl.innerText = "Failed to fetch signal.";
    console.error(err);
  }
}

fetchSignal();
