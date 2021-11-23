function createCard(project) {
	var dateNF = timeSince(project.detalhesDoproject.timepost);

    const card = `
        <div class="demoBlock" data-id="${project.onCoda}" style=${project.detalhesDoproject.orderList}>
        	<section class="painel_border__CodePost" style="border-color: ${project.detalhesDoproject.selectedColor}">

        		<div class="contentSendFor">
		            <img class="contentSendFor__perfil_img" src="${project.detalhesDoproject.user.imgUser}">
		            <p class="contentSendFor__perfil_name">${project.detalhesDoproject.user.nameUser}</p>
		            <p class="contentSendFor__timePost">${dateNF}</p>
		            <section class="box_bookmark">
		                <img class="contentSendFor__iconBookmark" src="assets/icons/bookmark_border_white_24dp.svg">
		            </section>
        		</div>

        		<section class="Info_project_Community">
				    <p class="descriptionProject">${project.detalhesDoproject.projectDescription}</p>
		        </section>

		        <section class="box_codePreview_FeedBacks">
		        	<div class="field_feedbacks">
		        		<div class="field_feedbacks__reports">
		        			<img class="icon_report" src="assets/icons/flag_white_24dp.svg">
		        			<p class="Text_ReportPost">Report</p>
		        		</div>
		        		<div class="field_feedbacks__commits">
		        			<img class="icons_feedback icon_commits" src="assets/icons/icon_feedBack.svg">
		        			<p class="num_feedbacks num_commits">${project.detalhesDoproject.numCommits}</p>
		        		</div>
		        		<div class="field_feedbacks__likes">
		        			<img class="icons_feedback icon_likes" onclick="markLike()" src="assets/icons/favorite_border_white_24dp.svg">
		        			<p class="num_feedbacks num_likes">${project.detalhesDoproject.numLikes}</p>
		        		</div>
		        	</div>
					<div class="painel_code__codePreview">
						<div class="box__buttons_decoration">
							<div class="button__decoration__red buttons__decoration"></div>
							<div class="button__decoration__yellow buttons__decoration"></div>
							<div class="button__decoration__green buttons__decoration"></div>
							<section class="label_language">
							    <label class="label_tagCode">${project.detalhesDoproject.selectedLanguagem}</label>										
							</section>
						</div>
						<div class="field_code">
						    <code onclick="fullView()" class="campo__code hljs ${project.detalhesDoproject.selectedLanguagem}"></code>		
						</div>
					</div>
				</section>

		    </section>
        </div>
    `
    return card
}