<script>
  import "../app.css";

  import CryptoComLogo from "../logo/crypto.svelte";
  import QuickenLogo from "../logo/quicken.svelte";
  import RightArrowIcon from "../icon/right-arrow.svelte";
  import { base } from "$app/paths";
</script>

<div class="h-screen bg-slate-900 text-gray-100 overflow-none flex flex-col">
  <div
    class="sticky top-0 z-40 w-full backdrop-blur flex-none transition-colors duration-500 lg:z-50 lg:border-b border-slate-50/[0.06] bg-white supports-backdrop-blur:bg-white/95 bg-slate-900/75">
    <div class="max-w-8xl mx-auto">
      <div
        class="py-4 border-b lg:px-8 lg:border-0 border-slate-300/10 mx-4 lg:mx-0">
        <div class="relative flex items-center">
          <a
            class="mr-3 flex items-center w-[2.0625rem] overflow-hidden md:w-auto"
            href={base}>
            <CryptoComLogo />
            <span class="ml-3 mr-4">
              <RightArrowIcon />
            </span>
            <QuickenLogo />
            <span class="ml-4 text-3xl font-light">Quickcro</span>
          </a>
          <div class="relative hidden lg:flex items-center ml-auto">
            <nav class="text-sm leading-6 font-semibold text-slate-200">
              <ul class="flex space-x-8">
                <li>
                  <a href={base} class="hover:text-sky-400">Convert</a>
                </li>
                <li>
                  <a class="hover:text-sky-400" href={`${base}/security`}
                    >Security</a>
                </li>
              </ul>
            </nav>
            <div class="flex items-center border-l ml-6 pl-6 border-slate-800">
              <a
                href="https://github.com/NoahCardoza/quickcro"
                class="block text-slate-400 hover:text-slate-300">
                <svg
                  viewBox="0 0 16 16"
                  class="w-5 h-5"
                  fill="currentColor"
                  aria-hidden="true">
                  <path
                    d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z" />
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <slot />
</div>
