require "yast/rake"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end

desc "Generate *-promo package files"
task :create_promo do
  Dir.chdir("package") do
    `./pre_checkin.sh`
  end
end

task :tarball => :create_promo

