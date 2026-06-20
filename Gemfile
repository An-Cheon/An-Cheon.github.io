# frozen_string_literal: true

source "https://rubygems.org"

gem "jekyll-theme-chirpy", "~> 7.2", ">= 7.2.4"

# C 扩展版 Liquid，加速模板渲染（约 990 页全量渲染的主要瓶颈）。
# 仅在 MRI（CI 的 Linux）上启用，避免本地 Windows 需要原生编译。
gem "liquid-c", "~> 4.0", platforms: [:ruby]

gem "html-proofer", "~> 5.0", group: :test

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.2.0", :platforms => [:mingw, :x64_mingw, :mswin]
