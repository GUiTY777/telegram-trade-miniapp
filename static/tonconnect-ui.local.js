
window.TonConnectUI = {
  TonConnectUI: function TonConnectUI(config) {
    const root = document.getElementById(config.buttonRootId);
    const button = document.createElement("button");
    button.innerText = "🔗 Подключить TON";
    button.className = "bg-green-600 text-white py-2 px-4 rounded-xl hover:bg-green-700";
    button.onclick = () => {
      const fakeWallet = {
        account: { address: "EQDUMMYADDRESSFAKEFAKE" }
      };
      TonConnectUI._callback?.(fakeWallet);
    };
    root.appendChild(button);

    this.onStatusChange = function (cb) {
      TonConnectUI._callback = cb;
    };
  }
};
