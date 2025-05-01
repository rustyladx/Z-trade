setInterval(async () => {
  const res = await fetch("/api/signal");
  const data = await res.json();
  document.getElementById("alerts").innerText = 
    `Signal: ${data.signal} ${data.symbol} at ${data.entry}`;
}, 5000);
