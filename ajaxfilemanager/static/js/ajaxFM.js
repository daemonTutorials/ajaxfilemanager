var ajaxFM = function(Y,cfg) {
    this.Y = Y;
    this.modalclass = cfg.modalclass;
    this.yesno_prefix = cfg.yesno_prefix;
    this.modal_path_prefix = cfg.modal_path_prefix;
};

ajaxFM.prototype = {
    showModal: function() {
        this.Y.one(this.modalclass).setStyle('display', 'block');
    },
    yesno: function(cfg) {
        this.Y.one('#'+this.yesno_prefix+'_head').set("innerHTML",cfg.title);
        this.Y.one('#'+this.yesno_prefix+'_details').set("innerHTML", cfg.msg);
        this.showModal();
    },
    modalPath: function(cfg) {
        this.Y.one('#'+this.modal_path_prefix+'_head').set("innerHTML",cfg.title);
        this.Y.one('#'+this.modal_path_prefix+'_details').set("innerHTML", cfg.msg);
        this.showModal();
    },
    setBookmarkTrigger: function(cfg) {
        this.Y.one(cfg.trigger).on('click', function() {
            if(this.Y.one(cfg.trigger).get('rel') == "off")
            {
                var marksAnim = new this.Y.Anim({
                    node: cfg.node,
                    to: {
                        opacity: 0,
                    },
                });        
                marksAnim.run();
                marksAnim.on('end', function() {
                    this.Y.one(cfg.node).setStyle('display', 'none');
                    this.Y.one(cfg.trigger+' span').set('innerHTML', 'on');
                    this.Y.one(cfg.trigger).set('rel', 'on');
                });
                localStorage.setItem('bkm_switch', 'off');
            }
            else {
                
                    this.Y.one(cfg.node).setStyle('display', 'block');
                var marksAnim = new this.Y.Anim({
                    node: cfg.node,
                    to: {
                        opacity: 1,
                    },
                });
                marksAnim.run();
                marksAnim.on('end', function() {
                    this.Y.one(cfg.trigger).set('rel', 'off');
                    this.Y.one(cfg.trigger+' span').set('innerHTML', 'off');
                });
                localStorage.setItem('bkm_switch', 'on');
            }
        });
    },
    setResetTrigger: function(cfg) {
        this.resetTrigger = cfg.trigger;
        this.Y.one(cfg.trigger).on('click', function() {
            var containerOut = new this.Y.Anim({
                node: 'body',
                to: {
                    opacity: 0,
                }
            });
            containerOut.run();
            containerOut.on('end', function() {
                
                this.Y.one('body').set('innerHTML', '');
                location.reload(true);
                
            });
        });
    },
};
