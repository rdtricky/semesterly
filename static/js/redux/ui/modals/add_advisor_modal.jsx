/*
Copyright (C) 2017 Semester.ly Technologies, LLC

Semester.ly is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Semester.ly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
*/

import PropTypes from 'prop-types';
import React from 'react';
import Modal from 'boron/WaveModal';
import * as SemesterlyPropTypes from '../../constants/semesterlyPropTypes';

class AddAdvisorModal extends React.Component {
  componentDidMount() {
    if (this.props.isVisible) {
      this.modal.show();
    }
  }

  componentDidUpdate() {
    if (this.props.isVisible) {
      this.modal.show();
    }
  }

  render() {
    const modalHeader =
      (<div className="modal-content">
        <div className="modal-header">
          <div
            className="header-pic"
            style={{ backgroundImage: 'url(/static/img/addtocalendarfeature.png)' }}
          />
          <h1>Add Advisor</h1>
          <div className="modal-close" onClick={() => this.modal.hide()}>
            <i className="fa fa-times" />
          </div>
        </div>
      </div>);
    const modalStyle = {
      width: '100%',
    };

    return (
      <Modal
        ref={(c) => { this.modal = c; }}
        className="add-advisor-modal abnb-modal max-modal"
        modalStyle={modalStyle}
        onHide={() => {
          this.props.toggleAddAdvisorModal();
          history.replaceState({}, 'Semester.ly', '/');
        }}
      >
        {modalHeader}
        <div className="add-advisor-modal__container">
          <p>Add Advisor Modal Stuff</p>
        </div>
      </Modal>
    );
  }
}

AddAdvisorModal.propTypes = {
  toggleAddAdvisorModal: PropTypes.func.isRequired,
  isVisible: PropTypes.bool.isRequired,
};

export default AddAdvisorModal;
