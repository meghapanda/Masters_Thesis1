var file=[["threshold-0.1_part-0_", 164], ["threshold-0.2_part-0_", 123], ["threshold-0.3_part-0_", 108], ["threshold-0.4_part-0_", 97], ["threshold-0.5_part-0_", 92], ["threshold-0.6_part-0_", 87], ["threshold-0.7_part-0_", 83], ["threshold-0.8_part-0_", 72], ["threshold-0.9_part-0_", 62]]
var path='/Users/meghapanda/Documents/Msc_Project/Code/hierarchical_full/'


var i, len,file_name,save_file_name;
for (i = 0, len = file.length, text = ""; i < len; i++) 
{
	file_name ='/Users/meghapanda/Documents/Msc_Project/Code/hierarchical_full/threshold-0.1_part-0_.dta'
	alert(file_name)
    save_file_name=file[i][0]+'_search.csv'
    iimSet("FLNM",file_name)
    iimPlay ('input.iim');
    var newURL = window.location.href;
	var test=newURL.includes('master_results.')
	// alert(newURL)
	while(test===false)
	{
		iimPlayCode("WAIT SECONDS=5");
		newURL = window.location.href;
		test=newURL.includes('master_results.')
	}
	iimSet("PATH",path)
    iimSet("SAVE_FLNM",save_file_name)

	if ( file[i][1]>300 ) 
		{
		iimPlay ('final_download_more_than_300.iim');
		} 
	else 
		{
		iimPlay ('final_download_less_than_300.iim');
		}
	
 
 
	
	
	
}