<script>
  import UploadIcon from "../icon/upload.svelte";
  import Papa from "papaparse";

  let files;

  function mmddyy(date) {
    var mm = date.getMonth() + 1; // getMonth() is zero-based
    var dd = date.getDate();

    return [
      (mm > 9 ? "" : "0") + mm,
      (dd > 9 ? "" : "0") + dd,
      date.getFullYear(),
    ].join("/");
  }

  function transformCSV(data) {
    return data.map(function (row) {
      const timestamp = new Date(row["Timestamp (UTC)"] + " UTC");
      const txDesc = row["Transaction Description"];
      const txAmount = row["Amount"];

      return {
        Date: mmddyy(timestamp),
        Description: txDesc,
        "Original Description": txDesc,
        Amount: txAmount,
        "Transaction Type": (parseFloat(txAmount) > 0 && "credit") || "debit",
        Category: (txDesc.endsWith(" -> USD") && "Transfer") || "Uncategorized",
        "Account Name": "Crypto.com Royal Indigo",
        Lables: "",
        Notes: "",
      };
    });
  }

  function downloadTextAsCSV(filename, text) {
    var blob = new Blob([text], { type: "text/csv;charset=utf-8;" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    setTimeout(function () {
      URL.revokeObjectURL(url);
    }, 100);
  }

  $: if (files) {
    const file = files[0];

    if (file) {
      const prefix = file.name.split(".");
      const extension = prefix.pop();

      Papa.parse(file, {
        header: true,
        skipEmptyLines: true,
        complete: function (results) {
          downloadTextAsCSV(
            [...prefix, "quicken", extension].join("."),
            Papa.unparse(transformCSV(results.data), {
              header: true,
              delimiter: ",",
            })
          );
        },
      });
    }
  }
</script>

<div class="flex items-center w-full h-full flex-col p-5">
  <div class="mb-8 text-xl">
    Convert your Crypto.com Debit Card CSV export to a Quicken ready CSV!
  </div>
  <div class="px-6 sm:px-0 sm:w-8/12 md:w-7/12 lg:w-6/12 xl:w-4/12">
    <div class="relative group w-full h-64 flex justify-center items-center">
      <div
        class="absolute inset-0 w-full h-full rounded-xl bg-gray-700 bg-opacity-80 shadow-2xl backdrop-blur-xl group-hover:bg-opacity-70 group-hover:scale-110 transition duration-300" />
      <input
        accept=".csv"
        class="relative z-10 opacity-0 h-full w-full cursor-pointer"
        type="file"
        name="input"
        id="input"
        bind:files />
      <div
        class="absolute top-0 right-0 bottom-0 left-0 w-full h-full m-auo flex items-center justify-center">
        <div class="space-y-6 text-center">
          <UploadIcon class="sm:w-16 w-16 m-auto fill-blue-300" />
          <p class="text-gray-100 text-lg">
            Drag and drop a file or <label
              for="dragOver"
              title="Upload a file"
              class="relative z-20 cursor-pointer block link"
              >Upload a file</label>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
