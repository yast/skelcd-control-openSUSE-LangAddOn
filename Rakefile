require "yast/rake"
require "fileutils"

Yast::Tasks.configuration do |conf|
  conf.obs_api = "https://api.opensuse.org"
  conf.obs_target = "openSUSE_13.2"
  conf.obs_sr_project = "openSUSE:13.2:Update"
  conf.obs_project = "YaST:openSUSE:13.2"
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end

# create pre-commit hook if missing
if !File.exist? ".git/hooks/pre-commit"
  FileUtils.ln_s "../../git-hooks/pre-commit.sh", ".git/hooks/pre-commit"
end

